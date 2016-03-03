(function () {
    'use strict';

    angular
        .module('app')
        .factory('tilesSvc', tilesSvc);

    tilesSvc.$inject = ['$http','appSettings'];

    function tilesSvc($http, appSettings) {

        return {
            getTileDetail: getTileDetail,
            getColorPallete: getColorPallete
        };

        function getTileDetail(tileId){
            return $http.get(appSettings.serverPath + 'tiles/' + tileId + '/order');
        }

        function getColorPallete() {
            return $http.get(appSettings.serverPath + 'palleteColors');
        }

    }
})();