(function () {
    'use strict';

    angular
        .module('app')
        .controller('tileDetailCtrl', tileDetailCtrl);

    tileDetailCtrl.$inject = ['$scope',
                              'tilesSvc',
                              'tilesLogicSvc',
                              'pageSettings',
                              'portfolioSvc',
                              '$modal',
                              'baseSettings',
                              'collectionsSvc'];

    function tileDetailCtrl($scope, tilesSvc, tilesLogicSvc, pageSettings, portfolioSvc, $modal, baseSettings, collectionsSvc) {
        var selectedTileId = $scope.shared.tileId;

        var vm = this;
        vm.labels = pageSettings.labels;
        vm.selectedWarehouse = vm.labels.shipFrom;
        vm.collection = $scope.shared.collection;
        vm.group = $scope.shared.group;
        vm.isAuthenticated = baseSettings.userIsAuthenticated;
        vm.navigation = baseSettings.navigation;
        vm.nortonImage = baseSettings.staticUrl + 'img/Norton-seal.png';
        vm.Order = {
            inputSqFt: 0,
            shipFromWarehouseId:0
        }

        vm.backToGroup = function () {
            $scope.shared.tileDetailTemplateUrl = '';
        };

        tilesSvc.getTileDetail(selectedTileId).then(function (response){
            vm.tile = response.data;
            vm.tile.quantityPerBox = tilesLogicSvc.calculateQuantityInBox(vm.tile);
            vm.tile.pricePerBox = tilesLogicSvc.calculatePricePerBox(vm.tile)
            if(vm.tile.sizes.length > 0){
                vm.selectedSize = vm.tile.sizes[0].size
            }
            
        });

        vm.showInstallationPhoto = function (tileId) {
            $modal.open({
                templateUrl: baseSettings.staticUrl + 'app/tiles/templates/tileModal.html',
                controller: 'tileModalCtrl',
                controllerAs: 'vm',
                size: 'lg',
                resolve: {
                    installationPhotos: function () {
                        return collectionsSvc.getInstallationPhoto(tileId).then(function (response) {
                            return response.data;
                        });
                    }
                }
            })
        };

        vm.saveToPortfolio = function (tileId) {
            portfolioSvc.addtile(tileId).then(function (response) {
                vm.tile.inPortfolio = true;
            });
        };

        vm.setSize = function (size) {
            vm.selectedSize = size.size;
        };

        vm.setWarehouse = function (warehouse) {
            vm.selectedWarehouse = warehouse.name;
        }

        vm.printPage = function () {
            print();
        }
    }
})();
