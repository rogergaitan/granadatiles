(function () {
    'use strict';

    angular
        .module('app.galleries')
        .factory('gallerySvc',['$http','appSettings', gallerySvc]);

    function gallerySvc($http, appSettings) {

        return {
            getGalleries: getGalleries
        };

        function getGalleries() {
            return $http.get(appSettings.serverPath + 'galleries');
        }

    }

}());