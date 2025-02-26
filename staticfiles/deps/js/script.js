

var galleryImages = document.querySelectorAll('.gallery-image');
var modal = document.getElementById('imageModal1');
var modalImage = document.getElementById('modalImage');

galleryImages.forEach(function(image) {
  image.addEventListener('click', function() {
    var imageUrl = this.getAttribute('src');
    modalImage.setAttribute('src', imageUrl);
    modal.style.display = 'block';
  });
});

$('.single-item').slick({
  centerMode: true,
  centerPadding: '400px',
  autoplay: true,
  autoplaySpeed: 2000,
  arrows: true,
  slidesToShow: 1,
  responsive: [
      {
          breakpoint: 1280,
          settings: {
              arrows: false,
              centerMode: true,
              centerPadding: '40px',
              slidesToShow: 1
          }
      },
      {
        breakpoint: 1920,
        settings: {
            arrows: false,
            centerMode: true,
            centerPadding: '350px',
            slidesToShow: 1
        }
    },
      {
          breakpoint: 720,
          settings: {
              arrows: false,
              centerMode: true,
              centerPadding: '10px',
              slidesToShow: 1
          }
      }
  ]
});
$('.indicators').on('click', function() {
  const index = $(this).data('slide-to'); 
  $('.single-item').slick('slickGoTo', index); 
  $('.indicator').removeClass('active');
  $(this).addClass('active'); 
});

// Обновление активного индикатора при смене слайда
$('.single-item').on('afterChange', function(event, slick, currentSlide) {
  $('.indicators').removeClass('active');
  $('.indicators').eq(currentSlide).addClass('active'); 
});

$('.carusel-imgage').slick({
  centerMode: true,
  centerPadding: '5px',
  slidesToShow: 3,
  responsive: [
    {
      breakpoint: 768,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: '40px',
        slidesToShow: 3
      }
    },
    {
      breakpoint: 480,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: '40px',
        slidesToShow: 3
      }
    }
  ]
});

// Устанавливаем активный индикатор при загрузке страницы
$('.indicators').first().addClass('active');
$(document).ready(function(){
  $('.slider').slick({
      dots: true, 
      infinite: true, 
      speed: 500, 
      slidesToShow: 1, 
      slidesToScroll: 1, 
      autoplay: true, 
      autoplaySpeed: 2000,
  });
});
$('.singles-item').slick({
  dots: false,
  infinite: false,
  speed: 300,
  slidesToShow: 5,
  slidesToScroll: 5,
  responsive: [
    {
      breakpoint: 1024,
      
      settings: {
        
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        dots: false
      }
    },
    {
      breakpoint: 600,
      dots: false,
      settings: {
        
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    }
    
  ]
});

function generateSlug() {
  const nameInput = document.getElementById('name');
  const slugInput = document.getElementById('slug');

  // Получаем значение из поля названия
  let slug = nameInput.value;

  // Преобразуем в нижний регистр, заменяем пробелы на дефисы и убираем не буквенно-цифровые символы
  slug = slug.toLowerCase()
             .trim()
             .replace(/[^a-z0-9]+/g, '-')
             .replace(/^-|-$/g, ''); 

  // Заполняем поле slug
  slugInput.value = slug;
}

document.getElementById('filter-toggle').addEventListener('click', function(event) {
  event.preventDefault();
  var filterBlock = document.getElementById('filter-block');

  if (filterBlock.style.display === 'none') {
      filterBlock.style.display = 'block';
  } else {
      filterBlock.style.display = 'none';
  }
});

function previewImage(event) {
  const input = event.target;
  const file = input.files[0];
  const imgElement = document.getElementById('avatar-image');

  if (file) {
      const reader = new FileReader();
      reader.onload = function(e) {
          imgElement.src = e.target.result;
      }
      reader.readAsDataURL(file); 
  }
}
function isMobileDevice() {
  return /Mobi|Android/i.test(navigator.userAgent);
}




$(document).ready(function () {

  $('input[name="tab-btn"]').on('change', function () {
      const checkedId = $(this).attr('id');
 
      $('input[name="custom-tab-btn"]').prop('checked', false);
      $('input[name="custom-tab-btn"][id="mobile-' + checkedId + '"]').prop('checked', true);
  });


  $('input[name="custom-tab-btn"]').on('change', function () {
      const checkedId = $(this).attr('id').replace('mobile-', '');
     
      $('input[name="tab-btn"]').prop('checked', false);
      $('input[name="tab-btn"][id="' + checkedId + '"]').prop('checked', true);
  });
});


document.addEventListener('DOMContentLoaded', function () {
  const galleryImages = document.querySelectorAll('.gallery-image');
  const modalImage = document.getElementById('modalImage');
  const modal = document.getElementById('imageModal2');

  galleryImages.forEach(image => {
      image.addEventListener('click', function () {
          modalImage.src = this.src; // Установите источник изображения в модальном окне
          modal.setAttribute('aria-hidden', 'false'); // Установите aria-hidden в false
          modal.style.display = 'block'; // Покажите модальное окно
      });
  });

  const closeButton = modal.querySelector('.btn-close');
  closeButton.addEventListener('click', function () {
      modal.setAttribute('aria-hidden', 'true'); // Установите aria-hidden в true
      modal.style.display = 'none'; // Скрыть модальное окно
  });
});