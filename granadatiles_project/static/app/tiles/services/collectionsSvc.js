(function () {
    'use strict';

    angular
        .module('app.tiles')
        .factory('collectionsSvc',
                ['appSettings',
                 '$http',
                collectionsSvc]);

    function collectionsSvc(appSettings, $http) {
        
        return {
            getCollections: getCollections,
            getMenuCollections: getMenuCollections,
            getFeaturedCollections: getFeaturedCollections
        }

        function getCollections() {
            return $http.get(appSettings.serverPath + 'collections');
        }

        function getMenuCollections(){
            return $http.get(appSettings.serverPath + 'collections/menu');
        }

        function getFeaturedCollections() {
            return $http.get(appSettings.serverPath + 'collections/featured');
        }

        
    }
}());