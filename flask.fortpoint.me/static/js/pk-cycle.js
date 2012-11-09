var cycler = {

    slides: false,
    current: false,
    paused: false,

    init: function(carouselID, carouselLeft, carouselRight) {

        this.slides = $(carouselID + ' .slides li');

        $(carouselLeft).click(function() {
            console.log('clicked left');
        });

        $(carouselRight).click(this.nextSlide);

        console.log('cycler initatied', this.slides);
    },

    nextSlide: function() {
        console.log('next');
    },

    prevSlide: function() {
        console.log('prev');
    }

};

$(function() {
    cycler.init('.carousel', '.scroll-left', '.scroll-right');

    $('.scroll-left').click(function() {
        console.log('clickerdedd');
    });
});


// $('#slidelist').cycle({
//     fx:     'fade',
//     speed:  '500',
//     timeout: 8000,
//     next: '#scroll-right',
//     prev: '#scroll-left'
// });

// $('#scroll-right, #scroll-left').click(function() {
//     $('#slidelist').cycle('pause');
// });
