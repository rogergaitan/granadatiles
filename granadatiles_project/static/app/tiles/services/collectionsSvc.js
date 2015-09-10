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
            getCollections: getCollections
        }

        function getCollections() {
            return $http.get(appSettings.serverPath + 'collections/');
        }
    }
})();