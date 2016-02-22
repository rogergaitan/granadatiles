(function () {
    'use strict';

    angular
        .module('app')
        .factory('cartSvc', cartSvc);

    cartSvc.$inject = ['$http', 'appSettings'];

    function cartSvc($http, appSettings) {
        var service = {
            getCartTilesCount: getCartTilesCount,
            getCartTiles: getCartTiles,
            addTile: addTile,
            updateTile: updateTile,
            addSample: addSample,
            removeTile: removeTile,
            getCartSamples: getCartSamples,
            addSample: addSample,
            updateSample: updateSample,
            removeSample: removeSample
        };

        return service;

        function getCartTilesCount() {
            return $http.get(appSettings.serverPath + 'cart/tiles_count')
        }

        function getCartTiles() {
            return $http.get(appSettings.serverPath + 'cart/tiles')
        }

        function addTile(tile) {
            return $http.post(appSettings.serverPath + 'cart/tiles', tile);
        }

        function updateTile(tile) {
            return $http.put(appSettings.serverPath + 'cart/tiles/' + tile.id);
        }

        function removeTile(tileId) {
            return $http.delete(appSettings.serverPath + 'cart/tiles/' + tileId);
        }

        function getCartSamples() {
            return $http.get(appSettings.serverPath + 'cart/samples')
        }

        function addSample(sample) {
            return $http.post(appSettings.serverPath + 'cart/samples', sample);
        }

        function updateSample(sample) {
            return $http.put(appSettings.serverPath + 'cart/samples/' + sample.id);
        }

        function removeSample(sampleId) {
            return $http.delete(appSettings.serverPath + 'cart/samples/' + sampleId);
        }

    }
})();