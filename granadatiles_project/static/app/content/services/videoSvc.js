(function () {
    'use strict';

    angular
        .module('app.content')
        .factory('videoSvc',['$http','appSettings',videoSvc]);

    function videoSvc($http, appSettings) {

        return {
            getVideos: getVideos
        };

        function getVideos() {
            return $http.get(appSettings.serverPath + 'videos');
        }

    }

}());