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
            getCollectionGroups: getCollectionGroups,
            getCollectionGallery: getCollectionGallery,
            getFilteredMenuCollection: getFilteredMenuCollection,
            getGroup: getGroup,
            getSizes: getSizes,
            getStyles: getStyles,
            getTiles: getTiles,
            getTileFilteredByStyle: getTileFilteredByStyle,
            getMainTile:getMainTile,
            getInstallationPhoto: getInstallationPhoto
        };

        function getCollections() {
            return $http.get(appSettings.serverPath + 'collections');
        }

        function getMenuCollections(){
            return $http.get(appSettings.serverPath + 'collections/menu');
        }

        function getFilteredMenuCollection(collectionId){
             return $http.get(appSettings.serverPath + 'collections/menu/?exclude='+ collectionId);
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

        function getCollectionGallery(collectionId) {
            return $http.get(appSettings.serverPath + 'collections/' + collectionId + '/installationphotos');
        }

        function getGroup(groupId) {
            return $http.get(appSettings.serverPath + 'groups/'+ groupId);
        }

        function getStyles(groupId){
            return $http.get(appSettings.serverPath + 'groups/' + groupId + '/styles');
        }

        function getSizes(groupId){
            return $http.get(appSettings.serverPath + 'groups/' + groupId + '/sizes');
        }

        function getTiles(groupId){
            return $http.get(appSettings.serverPath + 'groups/' + groupId + '/tiles')
        }

        function getTileFilteredByStyle(groupId, styleId){
            return $http.get(appSettings.serverPath + 'groups/' + groupId + '/tiles/?style=' + styleId)
        }

        function getMainTile(tileId){
            return $http.get(appSettings.serverPath + 'tiles/' + tileId);
        }

        function getInstallationPhoto(tileId){
            return $http.get(appSettings.serverPath + 'tiles/'+ tileId + '/installationphotos/')
        }
    }
}());
