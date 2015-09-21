/* =================================
   LOADER                     
=================================== */
// makes sure the whole site is loaded
jQuery(window).load(function () {
    // will first fade out the loading animation
    jQuery(".status").fadeOut();
    // will fade out the whole DIV that covers the website.
    jQuery(".preloader").delay(500).fadeOut("slow");
})

/* =================================
===  SHRINK NAVBAR              ====
=================================== */
$(window).scroll(function () {
    if ($(document).scrollTop() > 50) {
        $('#gt-header').addClass('shrink');
    } else {
        $('#gt-header').removeClass('shrink');
    }
});

/* =================================
===  WOW ANIMATION             ====
=================================== */

new WOW().init();
