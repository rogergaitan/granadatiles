(function () {
    'use strict';

    angular
        .module('app.tiles')
        .factory('instockSvc', instockSvc);

    instockSvc.$inject = ['$http', 'appSettings'];

    function instockSvc($http, appSettings) {
        var service = {
            getCollectionFilter: getCollectionFilter,
            getTiles: getTiles
        };

        return service;

        function getCollectionFilter() {
            return $http.get(appSettings.serverPath + 'tiles/collections_filters/');
        }

        function getTiles(collectionIds, isSample, offset) {
            return $http.get(appSettings.serverPath + 'tiles/in_stock_tiles/',
                {
                    params:
                        {
                            ids: collectionIds,
                            is_sample: isSample,
                            limit: 6,
                            offset: offset
                        }
                });
        }

    }
})();