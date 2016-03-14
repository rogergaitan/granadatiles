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
                              'cartSvc',
                              '$modal',
                              'baseSettings',
                              'collectionsSvc',
                              'gtUtilsSvc'];

    function tileDetailCtrl($scope, tilesSvc, tilesLogicSvc, pageSettings, portfolioSvc, cartSvc, $modal, baseSettings, collectionsSvc, gtUtilsSvc) {
        var selectedTileId = $scope.shared.tileId;
        gtUtilsSvc.addQueryStringParameter('tile', selectedTileId);

        var vm = this;
        vm.labels = pageSettings.labels;
        vm.selectedWarehouse = vm.labels.shipFrom;
        vm.collection = $scope.shared.collection;
        vm.group = $scope.shared.group;
        vm.isAuthenticated = baseSettings.userIsAuthenticated;
        vm.navigation = baseSettings.navigation;
        vm.nortonImage = baseSettings.staticUrl + 'img/Norton-seal.png';
        vm.order = {
            inputSqFt: 0,
            shipFromWarehouseId: 0,
            tilesNeeded: 0,
            tilesNeededOverage: 0,
            boxesNeeded: 0,
            baseCost: 0,
            discount: 0,
            shippingCost: 0,
            total: 0
        }

        vm.backToGroup = function () {
            $scope.shared.tileDetailTemplateUrl = '';
            gtUtilsSvc.removeQueryStringParameters();
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
            vm.order.shipFromWarehouseId = warehouse.id;
        }

        vm.printPage = function () {
            print();
        }

        vm.updateOrderDetail = function () {
            vm.order.tilesNeeded = vm.order.inputSqFt / parseFloat(vm.tile.sqFt.toPrecision(2));
            vm.order.tilesNeededOverage = Math.ceil(vm.order.tilesNeeded + ((vm.order.tilesNeeded) * 0.1));
            vm.order.boxesNeeded = Math.ceil(vm.order.tilesNeededOverage / vm.tile.box.quantity);
            vm.order.baseCost = vm.order.boxesNeeded * vm.tile.pricePerBox;
            vm.order.total = vm.order.baseCost + vm.order.shippingCost - vm.order.discount;
        }

        vm.addToCart = function () {
            if (vm.tile.sample) {
                var cartSample = {
                    quantity: vm.order.quantity,
                    id: vm.tile.id
                };
                cartSvc.addSample(cartSample).then(function (resp) {
                    window.location = pageSettings.navigation.cart;
                });
            }
            else {
                var cartItem = {
                    sqFt: vm.order.inputSqFt,
                    id: vm.tile.id
                };
                cartSvc.addTile(cartItem).then(function (resp) {
                    window.location = pageSettings.navigation.cart;
                });
            }
        };

    }
})();
