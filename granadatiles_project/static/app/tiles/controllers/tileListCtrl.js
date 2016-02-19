﻿(function () {
    'use strict';

    angular
        .module('app')
        .controller('tileListCtrl', tileListCtrl);

    tileListCtrl.$inject = ['baseSettings',
                            'pageSettings',
                            'collectionsSvc',
                            'flatPagesSvc',
                            '$modal',
                            '$scope'];

    function tileListCtrl(baseSettings, pageSettings, collectionsSvc, flatPagesSvc, $modal, $scope) {
        /* jshint validthis:true */
        var vm = this;

        vm.labels = pageSettings.labels;
        vm.subMenuCollapsed = true;
        vm.checkNew = false;
        vm.collectionAsideNavigationTemplateUrl = baseSettings.staticUrl + 'app/tiles/templates/collectionAsideNavigation.html';

        collectionsSvc.getCollection(pageSettings.collectionId).then(function (response) {
            vm.collection = response.data;
        });

        collectionsSvc.getCollectionGroups(pageSettings.collectionId).then(function (response) {
            vm.collectionGroups = response.data;
        });

        collectionsSvc.getFilteredMenuCollection(pageSettings.collectionId).then(function (response) {
            vm.filteredMenuCollection = response.data;
        });

        collectionsSvc.getGroup(pageSettings.groupId).then(function (response) {
            vm.group = response.data;
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

            if (vm.selectedStyle.id == 0) {
                collectionsSvc.getTiles(pageSettings.groupId).then(function (response) {
                    vm.tiles = response.data;
                });
            }
        });

        vm.setSize = function (size) {
            vm.selectedSize = size;
        };

        vm.setStyle = function (style) {
            vm.selectedStyle = style;
            updateTilesByStyle(style);
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

        function updateTilesByStyle(selectedStyle) {
            if (selectedStyle.id == 0) {
                collectionsSvc.getTiles(pageSettings.groupId).then(function (response) {
                    vm.tiles = response.data;
                });
            } else {
                collectionsSvc.getTileFilteredByStyle(pageSettings.groupId, selectedStyle.name).then(function (response) {
                    vm.tiles = response.data;
                });
            }
        };

        vm.updateTileByNew = function (checkNewValue) {
            (checkNewValue) ? console.log("intro") : console.log("not intro");
        };

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
            $scope.shared = {};
            $scope.shared.tileId = tileId;
            $scope.shared.tileDetailTemplateUrl = baseSettings.staticUrl + 'app/tiles/templates/tileDetails.html'
            $scope.shared.collection = vm.collection;
            $scope.shared.group = vm.group;
        };

        flatPagesSvc.getCollectionContentMenu(pageSettings.collectionId).then(function (response) {
            vm.collectionContent = response.data;
        });

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

    }
})();
