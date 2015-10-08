(function () {
    'use strict';

    angular
        .module('app.galleries')
        .factory('gallerySvc',['$http','appSettings', gallerySvc]);

    function gallerySvc($http, appSettings) {

        return {
            getGalleries: getGalleries,
            getGallery:getGallery
        };

        function getGalleries() {
            return $http.get(appSettings.serverPath + 'galleries');
        }

        function getGallery(categoryId) {
            return $http.get(appSettings.serverPath + 'galleriescategories/' + categoryId+ '/images');
        }

    }

}());