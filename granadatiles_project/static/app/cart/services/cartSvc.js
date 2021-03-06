﻿(function () {
    'use strict';

    angular
        .module('app')
        .factory('cartSvc', cartSvc);

    cartSvc.$inject = ['$http', 'appSettings'];

    function cartSvc($http, appSettings) {
        var service = {
            setCartCount: setCartCount,
            getCart: getCart,
            getCartTilesCount: getCartTilesCount,
            getCartTiles: getCartTiles,
            addTile: addTile,
            updateTile: updateTile,
            addSample: addSample,
            removeTile: removeTile,
            getCartSamples: getCartSamples,
            addSample: addSample,
            updateSample: updateSample,
            removeSample: removeSample,
            getCustomizedTiles: getCustomizedTiles,
            addCustomizedTile: addCustomizedTile,
            updateCustomizedTile: updateCustomizedTile,
            removeCusomizedTile: removeCusomizedTile
        };

        var cart = {
            count: 0
        };


        return service;

        function setCartCount(count) {
            cart.count = count;
        }

        function getCart(count) {
            return cart
        }

        function getCartTilesCount() {
            return $http.get(appSettings.serverPath + 'cart/tiles/count')
        }

        function getCartTiles() {
            return $http.get(appSettings.serverPath + 'cart/tiles')
        }

        function addTile(tile) {
            return $http.post(appSettings.serverPath + 'cart/tiles/', tile);
        }

        function updateTile(tile) {
            return $http.put(appSettings.serverPath + 'cart/tiles/' + tile.id, tile);
        }

        function removeTile(tileId) {
            return $http.delete(appSettings.serverPath + 'cart/tiles/' + tileId);
        }

        function getCartSamples() {
            return $http.get(appSettings.serverPath + 'cart/samples')
        }

        function addSample(sample) {
            return $http.post(appSettings.serverPath + 'cart/samples/', sample);
        }

        function updateSample(sample) {
            return $http.put(appSettings.serverPath + 'cart/samples/' + sample.id, sample);
        }

        function removeSample(sampleId) {
            return $http.delete(appSettings.serverPath + 'cart/samples/' + sampleId);
        }

        function getCustomizedTiles() {
            return $http.get(appSettings.serverPath + 'cart/customizedtiles');
        }

        function addCustomizedTile(customizedTile) {
            return $http.post(appSettings.serverPath + 'cart/customizedtiles/', customizedTile);
        }

        function updateCustomizedTile(customizedTile) {
            return $http.put(appSettings.serverPath + 'cart/customizedtiles/' + customizedTile.id, customizedTile);
        }

        function removeCusomizedTile(customizedTileId) {
            return $http.delete(appSettings.serverPath + 'cart/customizedtiles/' + customizedTileId);
        }

    }
})();