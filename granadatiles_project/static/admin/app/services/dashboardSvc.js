(function () {
    'use strict';

    angular
        .module('app')
        .service('dashboardSvc', dashboardSvc);

    dashboardSvc.$inject = ['$http', 'appSettings'];

    function dashboardSvc($http, appSettings) {
        this.getItemsCount = getItemsCount;
        this.getGroupsbycollectionChartData = getGroupsbycollectionChartData;
        this.getLatestUser = getLatestUser;

        function getItemsCount() {
            return $http.get(appSettings.serverPath + 'dashboard/itemcounts/');
        }

        function getGroupsbycollectionChartData(){
            return $http.get(appSettings.serverPath + 'dashboard/groupsbycollection/')
        }

        function getLatestUser() {
            return $http.get(appSettings.serverPath + 'dashboard/latestusers/')
        }
    }
})();