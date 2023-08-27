var slides = document.querySelectorAll('.slide');
var currentSlide = 0;

function showSlide(n) {
  slides[currentSlide].classList.remove('active');
  currentSlide = (n + slides.length) % slides.length;
  slides[currentSlide].classList.add('active');
}

setInterval(function () {
  showSlide(currentSlide + 1);
}, 2000);