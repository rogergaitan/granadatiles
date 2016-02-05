(function () {
    'use strict';

    angular
        .module('app.tiles')
        .factory('instockSvc', instockSvc);

    instockSvc.$inject = ['$http', 'appSettings'];

    function instockSvc($http, appSettings) {
        var service = {
            getCollectionFilter: getCollectionFilter,
            getSamples: getSamples,
            getTiles: getTiles
        };

        return service;

        function getCollectionFilter() {
            return $http.get(appSettings.serverPath + 'tiles/collections_filters/');
        }

        function getSamples() {
            return $http.get(appSettings.serverPath + 'tiles/in_stock_tiles/?is_sample=true');
        }

        function getTiles() {
            return $http.get(appSettings.serverPath + 'tiles/in_stock_tiles/');
        }

    }
})();