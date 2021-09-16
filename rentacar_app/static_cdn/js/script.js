$(window).on("scroll", function () {
    if ($(window).scrollTop()) {
        $('.navbar').addClass('half-white-on-scroll');
    } else {
        $('.navbar').removeClass('half-white-on-scroll');
    }
});
