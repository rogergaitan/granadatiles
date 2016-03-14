(function () {
    'use strict';

    angular
        .module('app')
        .controller('searchCtrl', searchCtrl);

    searchCtrl.$inject = ['pageSettings', 'searchSvc', 'gtUtilsSvc'];

    function searchCtrl(pageSettings, searchSvc, gtUtilsSvc) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;

        var searchTerm = gtUtilsSvc.getQueryStringParameterByName('searchTerm');

        searchSvc.search(searchTerm).then(function (response) {
            vm.searchResults = response.data;
        });
    }
})();
