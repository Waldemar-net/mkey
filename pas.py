import datetime
import requests
from bs4 import BeautifulSoup
import os
import re

from django.core.files import File
from django.core.files.base import ContentFile
from goods.models import RAMPC, Direx, Disk, Gallery, Languages, OCSystem, ProcessorPC, Products, Platforms, Publishers, Developers, Categories, Genre, Region, Services, VideoCard  # Импортируйте необходимые модели

months = {
    'января': '01',
    'февраля': '02',
    'марта': '03',
    'апреля': '04',
    'мая': '05',
    'июня': '06',
    'июля': '07',
    'августа': '08',
    'сентября': '09',
    'октября': '10',
    'ноября': '11',
    'декабря': '12'
}

def download_image(image_url):
    img_response = requests.get(image_url)
    if img_response.status_code == 200:
        return ContentFile(img_response.content)  # Возвращаем содержимое изображения
    else:
        print(f"Ошибка при скачивании изображения: {img_response.status_code}")
        return None

    
def sanitize_filename(name):
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo',
        'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
        'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
    }
    
    # Транслитерация текста
    translated_text = ''.join(translit_dict.get(char, char) for char in name)
    
    # Удаляем все, кроме букв, цифр и пробелов
    translated_text = re.sub(r'[^a-zA-Z0-9\s-]', '', translated_text)
    
    # Заменяем пробелы на дефисы и убираем лишние дефисы
    slug = re.sub(r'\s+', '-', translated_text).strip('-').lower()
    
    return slug

def parse_date_string(date_string):
    try:
        day, month_name, year = date_string.split()
        month = months[month_name]  # Получаем числовое значение месяца
        return f"{year}-{month}-{day.zfill(2)}"  # Форматируем в YYYY-MM-DD
    except (ValueError, KeyError) as e:
        print(f"Ошибка при преобразовании даты: {e}")
        return None  # Возвращаем None, если не удалось преобразовать дату

def process_multiple_values(value_string, model):
    values = [v.strip() for v in value_string.split(',')]
    objects = []
    for value in values:
        slug = sanitize_filename(value)
        obj, created = model.objects.get_or_create(
            name=value,
            defaults={'slug': slug}
        )
        objects.append(obj)
    return objects

def parse_website(url, classes):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        game_info = {}
        game_title = ""
        game_description = ""
        game_languages = {}

        subinfo_items = soup.find_all(class_='b-card__subinfo-item')
        for item in subinfo_items:
            title = item.find(class_='b-card__subinfo-head').get_text(strip=True)
            value = item.find(class_='b-card__subinfo-body').get_text(strip=True)
            game_languages[title] = value

        all_elements = soup.find_all(class_=classes)
        current_key = None

        for element in all_elements:
            text = element.get_text(strip=True)
            class_name = element.get('class')[0]
            if class_name == 'b-card__table-title':
                current_key = text
            elif class_name == 'b-card__table-value':
                value = text
                if current_key:
                    game_info[current_key] = value
            elif class_name == 'b-breadcrumbs__item':
                game_title = text
            elif class_name == 'b-card__tabdescription':
                game_description = text 
            elif class_name == 'b-card__subinfo-body':
                game_languages = text

        if game_title:
            game_info['Название'] = game_title

        # Скачиваем изображение из b-card__img (одно изображение)
        img_container = soup.find(class_='b-card__img')
        if img_container:
            img_tag = img_container.find('img', class_='js-img-bgcolro')
            if img_tag and 'src' in img_tag.attrs:
                image_url = img_tag['src']
                game_info['Изображение'] = download_image(image_url)  # Сохраняем изображение

        # Скачиваем изображения из js-fb (несколько изображений)
        fb_links = soup.find_all(class_='js-fb')
        counter = 1  # Счетчик для именования изображений
        images = []
        for fb_link in fb_links:
            img_tag = fb_link.find('img')
            if img_tag and 'src' in img_tag.attrs:
                image_url = img_tag['src']
                if not image_url.endswith('maxresdefault.jpg'):
                    images.append(download_image(image_url))  # Сохраняем изображения в список

        try:
            platform, created = Platforms.objects.get_or_create(name=game_info['Платформа'])
        except Exception as e:
            print(f"Ошибка при получении или создании платформы: {e}")
            platform = None

        try:
            rampc, created = RAMPC.objects.get_or_create(name=game_info['Оперативная память'])
        except Exception as e:
            print(f"Ошибка при получении или создании платформы: {e}")
            rampc = None

      

        try:
            publishers = process_multiple_values(game_info['Издатель'], Publishers)
        except Exception as e:
            print(f"Ошибка при получении или создании издателя: {e}")
            publishers = None

        try:
            developers = process_multiple_values(game_info['Разработчик'], Developers)
        except Exception as e:
            print(f"Ошибка при получении или создании разработчика: {e}")
            developers = None

        try:
            genres = process_multiple_values(game_info['Жанр'], Genre)
        except Exception as e:
            print(f"Ошибка при получении или создании жанра: {e}")
            genres = None

        try:
            system, created = OCSystem.objects.get_or_create(name=game_info['ОС'])
        except Exception as e:
            print(f"Ошибка при получении или создании издателя: {e}")
            system = None

        try:
            processor, created = ProcessorPC.objects.get_or_create(name=game_info['Процессор'])
        except Exception as e:
            print(f"Ошибка при получении или создании издателя: {e}")
            processor = None
          
        try:
            videocard, created = VideoCard.objects.get_or_create(name=game_info['Видеокарта'])
        except Exception as e:
            print(f"Ошибка при получении или создании издателя: {e}")
            videocard = None

        try:
            disk, created = Disk.objects.get_or_create(name=game_info['Место на диске'])
        except Exception as e:
            print(f"Ошибка при получении или создании издателя: {e}")
            disk = None

        try:
            languages, created = Languages.objects.get_or_create(name=game_languages['Поддержка языков'])
        except Exception as e:
            print(f"Ошибка при получении или создании издателя: {e}")
            languages = None

        try:
            region, created = Region.objects.get_or_create(name=game_languages['Регион активации'])
        except Exception as e:
            print(f"Ошибка при получении или создании издателя: {e}")
            region = None

        try:
            services, created = Services.objects.get_or_create(name=game_languages['Сервис активации'])
        except Exception as e:
            print(f"Ошибка при получении или создании издателя: {e}")
            services = None

        try:
            direx, created = Direx.objects.get_or_create(name=game_languages['DirectX'])
        except Exception as e:
            print(f"Ошибка при получении или создании издателя: {e}")
            direx = None
        
        # Сохраняем данные в базу данных
        if game_info:

            release_date = parse_date_string(game_info['Дата выхода'])

            
            additional = game_info.get('Дополнительно', None)
            

            product, created = Products.objects.get_or_create(
                name=game_info['Название'],
                defaults={
                    'slug': sanitize_filename(game_info['Название']),
                    'description': game_description, 
                    'platform' : platform,
                    'rampc' : rampc,
                    'datas' : release_date,
                    'system' : system,
                    'processor' : processor,
                    'videocard' : videocard,
                    'additional' : additional,
                    'disk' : disk,
                    'languages' : languages,
                    'region' : region,
                    'services' : services,
                    'direx' : direx
            

                
                }
            )
            for publisher in publishers:
                product.publisher.add(publisher)

            # Добавляем разработчиков
            for developer in developers:
                product.developer.add(developer)

            # Добавляем жанры
            for genry in genres:
                product.genry.add(genry)

            # Сохраняем основное изображение
            if 'Изображение' in game_info and game_info['Изображение']:
                product.image.save(f"{sanitize_filename(game_info['Название'])}.jpg", game_info['Изображение'])

            # Сохраняем дополнительные изображения в галерее
            for img_content in images:
                if img_content:
                    gallery_image = Gallery.objects.create(product=product)
                    gallery_image.image.save(f"{counter}.jpg", img_content)
                    counter += 1

            product.save()  # Сохраняем продукт

    else:
        print(f"Ошибка при запросе страницы: {response.status_code}")