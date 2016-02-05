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
        vm.isSample = false;

        if (pageSettings.samples) {
            vm.isSample = true;
            instockSvc.getSamples().then(function (response) {
                vm.tiles = response.data;
            });
        }
        else {
            instockSvc.getTiles().then(function (response) {
                vm.tiles = response.data;
            })
        }

        instockSvc.getCollectionFilter(function (response) {
            vm.collectionFilters = response.data;
        });

        sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
            vm.section = response.data;
        });

    }
})();
