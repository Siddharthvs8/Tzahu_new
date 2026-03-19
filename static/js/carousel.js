document.addEventListener('DOMContentLoaded', () => {
  const carousels = document.querySelectorAll('.carousel');
  carousels.forEach((c) => {
    const track = c.querySelector('.carousel-track');
    const slides = c.querySelectorAll('.slide');
    const prev = c.querySelector('.nav.prev');
    const next = c.querySelector('.nav.next');
    const dotsWrap = c.querySelector('.dots');
    let index = 0;
    const intervalMs = parseInt(c.dataset.interval || '5000', 10);
    const autoplay = c.dataset.autoplay === 'true';

    slides.forEach((_, i) => {
      const b = document.createElement('button');
      b.addEventListener('click', () => go(i));
      dotsWrap.appendChild(b);
    });

    function update(){
      track.style.transform = `translateX(${-index * 100}%)`;
      dotsWrap.querySelectorAll('button').forEach((b, i) => {
        b.classList.toggle('active', i === index);
      });
    }
    function go(i){ index = (i + slides.length) % slides.length; update(); }
    function nextSlide(){ go(index + 1); }
    function prevSlide(){ go(index - 1); }

    prev && prev.addEventListener('click', prevSlide);
    next && next.addEventListener('click', nextSlide);

    update();

    if (autoplay && slides.length > 1){
      setInterval(nextSlide, intervalMs);
    }
  });
});
