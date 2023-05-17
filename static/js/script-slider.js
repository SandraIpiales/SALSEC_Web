 
var swiper = new Swiper(".slide-content", {
  slidesPerView: 4,
  spaceBetween: 25,
  
  centerSlide: 'true',
  fade: 'true',
  grabCursor: 'true',
  grabCursor: true,
  keyboard: {
    enabled: true,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  breakpoints:{
      0: {
          slidesPerView: 1,
      },
      550: {
          slidesPerView: 2,
      },
      950:{
        slidesPerView: 3,
      },
      1200: {
          slidesPerView: 4,
      },
  },
});
