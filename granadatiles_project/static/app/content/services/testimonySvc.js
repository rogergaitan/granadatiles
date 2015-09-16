(function () {
    'use strict';
    
    angular
        .module('app.content')
        .factory('testimonySvc',
                   ['$http',
                    'appSettings',
                    testimonySvc]);

    function testimonySvc($http, appSettings) {

        return {
            getTestimonials: getTestimonials
        }

        function getTestimonials() {
            return $http.get(appSettings.serverPath + 'testimonials');
        }

    };

}());