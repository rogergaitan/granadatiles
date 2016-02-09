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
            getFlatPagesMenu: getFlatPagesMenu
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

        return service
       
    }
})();