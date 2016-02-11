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
            vm.offset = 0;
            UpdateTiles(true);
        };

        vm.nextPage = function () {
            if (!vm.inProgress) {
                vm.offset = vm.tiles.length;
                UpdateTiles(false);
            }
        }

        function UpdateTiles(reset) {
            vm.inProgress = true;
            instockSvc.getTiles(vm.selectedCollectionFilters, vm.isSample, vm.offset)
                .then(function (response) {
                    if (!vm.tiles || reset) {
                        vm.tiles = response.data;
                    }
                    else {
                        for (var i = 0; i < response.data.length; i++) {
                            vm.tiles.push(response.data[i]);
                        }
                    }
                    vm.inProgress = false;
                });
        }

    }
})();
