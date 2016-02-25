(function () {
    'use strict';

    angular
        .module('app')
        .factory('tilesSvc', tilesSvc);

    tilesSvc.$inject = ['$http','appSettings'];

    function tilesSvc($http, appSettings) {

        return {
           getTileDetail: getTileDetail
        };

        function getTileDetail(tileId){
            return $http.get(appSettings.serverPath + 'tiles/' + tileId + '/order');
        }

    }
})();