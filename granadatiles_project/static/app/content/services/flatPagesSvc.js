(function () {
    'use strict';

    angular
        .module('app.content')
        .factory('flatPagesSvc', flatPagesSvc);

    flatPagesSvc.$inject = ['$http', 'appSettings'];

    function flatPagesSvc($http, appSettings ) {
        var service = {
            getFlatPageCover:getFlatPageCover,
            getFlatPage: getFlatPage,
            getFlatPagesMenu: getFlatPagesMenu,
            getCollectionContent: getCollectionContent,
            getCollectionContentMenu: getCollectionContentMenu
        };

        function getFlatPageCover(pageTitle) {
            return $http.get(appSettings.serverPath + 'flatpages/' + pageTitle + '/cover')
        }

        function getFlatPage(pageTitle) {
            return $http.get(appSettings.serverPath + 'flatpages/' + pageTitle);
        }

        function getFlatPagesMenu(menuId) {
            return $http.get(appSettings.serverPath + 'flatpages/?menuId=' + menuId);
        }

        function getCollectionContent(pageTitle) {
            return $http.get(appSettings.serverPath + 'collection_content/' + pageTitle);
        }

        function getCollectionContentMenu(collectionId) {
            return $http.get(appSettings.serverPath + 'collection_content/?collectionId=' + collectionId);
        }

        return service
       
    }
})();