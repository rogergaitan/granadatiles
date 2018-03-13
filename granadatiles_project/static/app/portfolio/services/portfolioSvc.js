(function () {
    'use strict';

    angular
        .module('app.portfolio')
        .factory('portfolioSvc', portfolioSvc);

    portfolioSvc.$inject = ['$http', 'appSettings'];

    function portfolioSvc($http, appSettings) {

        var service = {
            getPortfolioTiles: getPortfolioTiles,
            getPortfolioTile: getPortfolioTile,
            addtile: addtile,
            removeTile: removeTile
        };

        return service;

        function getPortfolioTiles() {
            return $http.get(appSettings.serverPath + 'portfolio/tiles');
        }

        function getPortfolioTile(tileId) {
            return $http.get(appSettings.serverPath + 'portfolio/tiles/' + tileId);
        }

        function addtile(tileId) {
            return $http.post(appSettings.serverPath + 'portfolio/tiles/',
                {
                    id:tileId
                });
        }

        function removeTile(tileId, isCustomTile) {
            var queryString = '';
            if (isCustomTile)
                queryString = '?isCustomTile=true';
            return $http.delete(appSettings.serverPath + 'portfolio/tiles/' + tileId + queryString);
        }
    }
})();