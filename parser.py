import requests
from bs4 import BeautifulSoup
import os
import re

def download_image(image_url, save_path):
    img_response = requests.get(image_url)
    if img_response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(img_response.content)
        print(f"Изображение сохранено: {save_path}")
    else:
        print(f"Ошибка при скачивании изображения: {img_response.status_code}")

def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def parse_website(url, classes):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        game_info = {}
        game_title = ""
        game_discription = ""
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
                game_discription = text
            elif class_name == 'b-card__subinfo-item':
                value = text
                if current_key:
                    game_languages[current_key] = value
                

        if game_title:
            game_info['Название'] = game_title

        if game_info:
            for key, value in game_info.items():
                print(f"{key} - {value}")

        if game_languages:
           for key, value in game_languages.items():
                print(f"{key} - {value}")
          
                
        if game_discription:
            print('Описание: '+game_discription)
        else:
            print("Информация о игре не найдена.")

        # Скачиваем изображение из b-card__img (одно изображение)
        img_container = soup.find(class_='b-card__img')
        if img_container:
            img_tag = img_container.find('img', class_='js-img-bgcolro')
            if img_tag and 'src' in img_tag.attrs:
                image_url = img_tag['src']
                image_name = os.path.basename(image_url)
                safe_game_title = sanitize_filename(game_info['Название'])
                save_directory = os.path.join('images', safe_game_title)
                os.makedirs(save_directory, exist_ok=True)
                save_path = os.path.join(save_directory, image_name)
                download_image(image_url, save_path)

        # Скачиваем изображения из js-fb (несколько изображений)
        fb_links = soup.find_all(class_='js-fb')
        counter = 1  # Счетчик для именования изображений
        for fb_link in fb_links:
            img_tag = fb_link.find('img')
            if img_tag and 'src' in img_tag.attrs:
                image_url = img_tag['src']
                
                # Проверяем, чтобы изображение не заканчивалось на maxresdefault.jpg
                if not image_url.endswith('maxresdefault.jpg'):
                    # Формируем имя файла с учетом счетчика
                    image_name = f"{counter}.jpg"
                    safe_game_title = sanitize_filename(game_info['Название'])
                    save_directory = os.path.join('images', safe_game_title)
                    os.makedirs(save_directory, exist_ok=True)
                    save_path = os.path.join(save_directory, image_name)
                    download_image(image_url, save_path)
                    counter += 1  # Увеличиваем счетчик

    else:
        print(f"Ошибка при запросе страницы: {response.status_code}")

# Пример использования
url = 'https://gabestore.ru/game/ready-or-not-lspd-edition'
classes_to_parse = ['b-card__table-value', 'b-card__table-title', 'b-breadcrumbs__item', 'b-card__tabdescription', 'b-card__subinfo-item']
parse_website(url, classes_to_parse)