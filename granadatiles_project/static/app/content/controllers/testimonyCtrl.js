(function () {
    'use strict';

    angular
        .module('app.content')
        .controller('testimonyCtrl',
                    ['testimonySvc',
                    'pageSettings',
                     testimonyCtrl]);

    function testimonyCtrl(testimonySvc, pageSettings) {
        var vm = this;

        testimonySvc.getTestimonials().then(function (response) {
            vm.testimonials = response.data;
        });

        vm.labels = pageSettings.labels;

    }
        
}());