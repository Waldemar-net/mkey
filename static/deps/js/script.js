$(document).ready(function(){
    $('.carusel-imgage').slick({
        lazyLoad: 'ondemand',
        slidesToShow: 3,
        slidesToScroll: 1
    });
});

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
  centerPadding: '450px',
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

$('.singles-item').slick({
  dots: false,
  infinite: false,
  speed: 300,
  slidesToShow: 4,
  slidesToScroll: 4,
  responsive: [
    {
      breakpoint: 1024,
      
      settings: {
        
        slidesToShow: 2,
        slidesToScroll: 2,
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
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
});

document.getElementById("id_image").addEventListener("change", function() {
  var file = this.files[0];
  if (file) {
    var reader = new FileReader();
    reader.onload = function(event) {
      document.getElementById("avatar-image").src = event.target.result;
    };
    reader.readAsDataURL(file);
  }
});