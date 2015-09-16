(function () {
    'use strict';

    angular
        .module('app.content')
        .controller('testimonyCtrl',
                    ['testimonySvc',
                    'areaSvc',
                     testimonyCtrl]);

    function testimonyCtrl(testimonySvc, areaSvc) {
        var vm = this;

        testimonySvc.getTestimonials().then(function (response) {
            vm.testimonials = response.data;
        });

        vm.intro = 'Read what our architect, designer, and homeowner clients say';

    }
        
}());