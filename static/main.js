$(document).ready(function () {

  $('.corusel').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,

  });

  $('.more_color').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: '.corusel',
    dots: false,
    adaptiveHeight: true,
    infinite: false,
    variableWidth: true,
  });
  $('.more_color .slick-slide').on('click', function (event) {
    $('.corusel').slick('slickGoTo', $(this).data('slickIndex'));
  });

})