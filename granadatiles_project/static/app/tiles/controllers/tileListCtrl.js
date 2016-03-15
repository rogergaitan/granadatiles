(function () {
    'use strict';

    angular
        .module('app')
        .controller('tileListCtrl', tileListCtrl);

    tileListCtrl.$inject = ['baseSettings',
                            'pageSettings',
                            'collectionsSvc',
                            'flatPagesSvc',
                            '$modal',
                            '$scope',
                            'gtUtilsSvc',
                            'cartSvc',
                            '$q'];

    function tileListCtrl(baseSettings, pageSettings, collectionsSvc, flatPagesSvc, $modal, $scope, gtUtilsSvc, cartSvc, $q) {
        /* jshint validthis:true */
        var vm = this;

        vm.labels = pageSettings.labels;
        vm.subMenuCollapsed = true;
        vm.onlyNews = false;
        vm.collectionAsideNavigationTemplateUrl = baseSettings.staticUrl + 'app/tiles/templates/collectionAsideNavigation.html';
        vm.offset = 0;
        $scope.shared = {};

        var collection = collectionsSvc.getCollection(pageSettings.collectionId)

        var group = collectionsSvc.getGroup(pageSettings.groupId)

        $q.all([collection, group]).then(function (response) {
            vm.collection = response[0].data;
            vm.group = response[1].data;
            var selectedTileId = gtUtilsSvc.getQueryStringParameterByName('tile');
            if (selectedTileId)
                vm.showTileDetail(selectedTileId);
        });

        collectionsSvc.getCollectionGroups(pageSettings.collectionId).then(function (response) {
            vm.collectionGroups = response.data;
        });

        collectionsSvc.getFilteredMenuCollection(pageSettings.collectionId).then(function (response) {
            vm.filteredMenuCollection = response.data;
        });

        vm.selectedStyle = {
            'id': 0,
            'name': vm.labels.all
        };

        UpdateTiles(false);

        vm.refreshTiles = function () {
            vm.offset = 0;
            UpdateTiles(true);
        };

        vm.nextPage = function () {
            if (!vm.inProgress && !$scope.shared.tileDetailTemplateUrl) {
                vm.offset = vm.tiles.length;
                UpdateTiles(false);
            }
        }

        function UpdateTiles(reset) {
            vm.inProgress = true;
            collectionsSvc.getTiles(pageSettings.groupId,
                                    vm.offset,
                                    vm.onlyNews,
                                    vm.onlyInStock,
                                    vm.onlySpecials,
                                    vm.selectedStyle.id)
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

        flatPagesSvc.getCollectionContentMenu(pageSettings.collectionId).then(function (response) {
            vm.collectionContent = response.data;
        });

        collectionsSvc.getStyles(pageSettings.groupId).then(function (response) {
            vm.styles = response.data;
            vm.updatedStyles = [];
            vm.updatedStyles.push({
                'id': 0,
                'name': vm.labels.all
            });
            for (var i = 0; i < vm.styles.length; i++) {
                vm.updatedStyles.push(vm.styles[i]);
            }
            vm.selectedStyle = vm.updatedStyles[0];
        });

        vm.setStyle = function (style) {
            vm.selectedStyle = style;
            UpdateTiles(true);
        };

        vm.setTile = function (index, tileId) {
            collectionsSvc.getMainTile(tileId).then(function (response) {
                var arrayTiles = [];
                for (var i = 0; i < vm.tiles[index].tiles.length; i++) {
                    if (vm.tiles[index].tiles[i].id != tileId) {
                        arrayTiles.push(vm.tiles[index].tiles[i])
                    }
                }
                arrayTiles.push({
                    'id': vm.tiles[index].main.id,
                    'name': vm.tiles[index].main.name,
                    'image': vm.tiles[index].main.image,
                    'sizes': vm.tiles[index].main.sizes,
                    'hasInstallationPhotos': vm.tiles[index].main.hasInstallationPhotos,
                    'hasSample': vm.tiles[index].main.hasSample
                });
                vm.tiles[index].tiles = arrayTiles;
                vm.main = response.data;
                vm.tiles[index].previousImage = vm.tiles[index].main.mosaic;
                updateMain(index, vm.main);
            });
        };

        function updateMain(index, main) {
            var setMain = [];
            setMain.push({
                'id': main.id,
                'name': main.name,
                'mosaic': main.mosaic,
                'image': main.image,
                'sizes': main.sizes,
                'hasInstallationPhotos': main.hasInstallationPhotos,
                'hasSample': main.hasSample
            });
            vm.tiles[index].main = setMain[0];
        }

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

        vm.showTileDetail = function (tileId) {
            $scope.shared.tileId = tileId;
            $scope.shared.tileDetailTemplateUrl = baseSettings.staticUrl + 'app/tiles/templates/tileDetails.html'
            $scope.shared.collection = vm.collection;
            $scope.shared.group = vm.group;
        };

        vm.showCollectionGallery = function () {
            $modal.open({
                templateUrl: baseSettings.staticUrl + 'app/tiles/templates/tileModal.html',
                controller: 'tileModalCtrl',
                controllerAs: 'vm',
                size: 'lg',
                resolve: {
                    installationPhotos: function () {
                        return collectionsSvc.getCollectionGallery(pageSettings.collectionId).then(function (response) {
                            return response.data;
                        });
                    }
                }
            })
        };

        vm.orderFreeSample = function (tile) {
            var cartSample = {
                quantity: 1,
                id: tile.sampleId
            };
            cartSvc.addSample(cartSample).then(function (resp) {
                //window.location = pageSettings.navigation.cart;
            });
        }

    }
})();
