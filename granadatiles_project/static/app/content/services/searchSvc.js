(function () {
    'use strict';

    angular
        .module('app')
        .factory('searchSvc', searchSvc);

    searchSvc.$inject = ['$http', 'appSettings'];

    function searchSvc($http, appSettings) {
        var service = {
            search: search
        };

        return service;

        function search(searchTerm) {
            return $http.get(appSettings.serverPath + 'search/?searchTerm=' + searchTerm);
        }
    }
})();