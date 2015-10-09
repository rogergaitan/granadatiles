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
            getFeaturedCollections: getFeaturedCollections,
            getCollection: getCollection,
            getCollectionGroups: getCollectionGroups
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

        function getCollection(collectionId){
            return $http.get(appSettings.serverPath + 'collections/'+ collectionId);
        }

        function getCollectionGroups(collectionId) {
            return $http.get(appSettings.serverPath + 'collections/'+ collectionId + '/groups');
        }

        
    }
}());