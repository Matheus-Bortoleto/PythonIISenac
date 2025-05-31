const slider = document.querySelector('.slider');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
let slideIndex = 0;

function nextSlide() {
    slideIndex = (slideIndex + 1) % 2; // 2 é o número de slides
    updateSlider();
}

function prevSlide() {
    slideIndex = (slideIndex - 1 + 2) % 2;
    updateSlider();
}

function updateSlider() {
    slider.style.transform = `translateX(-${slideIndex * 100}%)`;
}

nextBtn.addEventListener('click', nextSlide);
prevBtn.addEventListener('click', prevSlide);