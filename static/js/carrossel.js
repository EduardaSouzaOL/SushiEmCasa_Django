document.addEventListener('DOMContentLoaded', function () {
    const track = document.querySelector('.carrossel-track');
    
    if (!track) return;

    const slides = Array.from(track.children);
    const nextButton = document.querySelector('.seta-direita');
    const prevButton = document.querySelector('.seta-esquerda');
    const slideWidth = slides[0].getBoundingClientRect().width;

    let currentIndex = 0;

   
    const moveToSlide = (targetIndex) => {
        track.style.transform = 'translateX(-' + slideWidth * targetIndex + 'px)';
        currentIndex = targetIndex;
    }

    
    nextButton.addEventListener('click', () => {
        let nextIndex = currentIndex + 1;
        if (nextIndex >= slides.length) {
            nextIndex = 0; 
        }
        moveToSlide(nextIndex);
    });

    
    prevButton.addEventListener('click', () => {
        let prevIndex = currentIndex - 1;
        if (prevIndex < 0) {
            prevIndex = slides.length - 1;
        }
        moveToSlide(prevIndex);
    });
});