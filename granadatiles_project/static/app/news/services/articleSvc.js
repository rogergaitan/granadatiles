(function () {
    'use strict';

    angular
        .module('app.news')
        .factory('articleSvc', ['$http', 'appSettings', articleSvc]);

    function articleSvc($http, appSettings) {

        return {
            getArticles: getArticles
        };

        function getArticles() {
            return $http.get(appSettings.serverPath + 'news/articles');
        }
    }
}());