$(window).load(function () {

    "use strict";

    /* *****************************************************************
     * ENABLE SMOOTH SCROLL
     * ************************************************************** */

    $('.btn-link,.nav-wrapper .main-nav li a,.nav-wrapper .side-nav li a').smoothScroll({offset: -50, speed: 1200});


    /* *****************************************************************
     * SCROLL TOP
     * ************************************************************** */

    $(window).scroll(function () {
        if ($(window).scrollTop() > ($('#home').height()) + 50) {
            $('.scroll-to-top').fadeIn(200);
        } else {
            $('.scroll-to-top').fadeOut(200);
        }
    });

    $('.scroll-to-top').on('click', function(event) {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: 0
        }, 1000);
    });








});