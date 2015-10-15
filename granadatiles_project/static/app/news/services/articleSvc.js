(function () {
    'use strict';

    angular
        .module('app.news')
        .factory('articleSvc', ['$http', 'appSettings', articleSvc]);

    function articleSvc($http, appSettings) {

        return {
            getArticles: getArticles,
            getYears: getYears,
            getArticlesFiltered: getArticlesFiltered
        };

        function getArticles() {
            return $http.get(appSettings.serverPath + 'news/articles');
        }

        function getYears() {
            return $http.get(appSettings.serverPath + 'news/articles/years/');
        }

        function getArticlesFiltered(selectedYear) {
            return $http.get(appSettings.serverPath + 'news/articles/?years=' + selectedYear);
        }
    }
}());