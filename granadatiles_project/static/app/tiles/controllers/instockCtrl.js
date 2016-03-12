(function () {
    'use strict';

    angular
        .module('app.tiles')
        .controller('instockCtrl', instockCtrl);

    instockCtrl.$inject = ['baseSettings', 'pageSettings', 'instockSvc', 'sectionSvc', '$scope'];

    function instockCtrl(baseSettings, pageSettings, instockSvc, sectionSvc, $scope) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.navigation = pageSettings.navigation;
        vm.isSample = (pageSettings.samples) ? true : false;
        $scope.shared = {};
        $scope.shared.inStockType = (pageSettings.samples) ? vm.labels.samples : vm.labels.tiles;
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

        vm.showTileDetail = function (tileId) {
            $scope.shared.tileId = tileId;
            $scope.shared.tileDetailTemplateUrl = baseSettings.staticUrl + 'app/tiles/templates/tileDetails.html'
        };

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
