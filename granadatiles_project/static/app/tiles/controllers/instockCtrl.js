(function () {
    'use strict';

    angular
        .module('app.tiles')
        .controller('instockCtrl', instockCtrl);

    instockCtrl.$inject = ['pageSettings', 'instockSvc', 'sectionSvc'];

    function instockCtrl(pageSettings, instockSvc, sectionSvc) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.navigation = pageSettings.navigation;
        vm.isSample = (pageSettings.samples) ? true : false;

        UpdateTiles();

        instockSvc.getCollectionFilter().then(function (response) {
            vm.collectionFilters = response.data;
        });

        sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
            vm.section = response.data;
        });

        vm.selectedCollectionFilters = [];

        vm.refreshTiles = function () {
            UpdateTiles();
        };

        function UpdateTiles() {
            instockSvc.getTiles(vm.selectedCollectionFilters, vm.isSample)
                .then(function (response) {
                    vm.tiles = response.data;
                });
            }

    }
})();
