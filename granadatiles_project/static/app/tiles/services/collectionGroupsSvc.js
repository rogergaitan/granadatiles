(function () {
    'use strict';

    angular
        .module('app.tiles')
        .factory('collectionGroupsSvc',['$http','appSettings', collectionGroupsSvc]);

    function collectionGroupsSvc($http, appSettings) {

        return {
            getCollectionGroups: getCollectionGroups
        };

        function getCollectionGroups(collectionId) {
            return $http.get(appSettings.serverPath + 'collections/'+ collectionId + '/groups');
        }

    }

}());
