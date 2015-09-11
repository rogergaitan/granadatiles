(function () {
    "use strict";

    angular
        .module('app.tiles')
        .factory('collectionsSvc',
                ['appSettings',
                 '$http',
                collectionsSvc]);

    function collectionsSvc(appSettings, $http) {
        
        return {
            getCollections: getCollections,
            getMenuCollections: getMenuCollections
        }

        function getCollections() {
            return $http.get(appSettings.serverPath + 'collections/');
        }

        function getMenuCollections(){
            return $http.get(appSettings.serverPath + 'collections/menu');
        }

        
    }
})();