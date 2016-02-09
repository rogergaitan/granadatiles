(function () {
    'use strict';

    angular
        .module('app.tiles')
        .controller('collectionsGroupCtrl',
                    ['baseSettings',
                     'pageSettings',
                     'collectionsSvc',
                     '$modal',
                     '$scope',
                     '$timeout',
                     collectionsGroupCtrl
                    ]);

    function collectionsGroupCtrl(baseSettings,
                                  pageSettings,
                                  collectionsSvc,
                                  $modal,
                                  $scope,
                                  $timeout) {
        var vm = this;

        vm.labels = pageSettings.labels;

        vm.subMenuCollapsed = true;

        vm.checkNew = false;

        vm. arrayFilter = [];

        vm.filterValue = 0;

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

        if (pageSettings.groupId >= 0) {
            collectionsSvc.getGroup(pageSettings.groupId).then(function (response) {
                vm.group = response.data;
            });
        }

        /*collectionsSvc.getTiles(pageSettings.groupId).then(function (response) {
            vm.tiles = response.data;
        });*/

        //vm.tiles = collectionsSvc.getTiles(pageSettings.groupId);

        /*collectionsSvc.getSizes(pageSettings.groupId).then(function (response) {
            vm.sizes = response.data;
            //vm.selectedSize = vm.sizes[0];
        });*/

        if (pageSettings.groupId >= 0) {
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
        }

        vm.setSize = function (size) {
            vm.selectedSize = size;
        };

        vm.setStyle = function (style) {
            vm.selectedStyle = style;
            //updateTilesByStyle(style);
            updateTiles( vm.filterValue = 5,style);
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
        }

        vm.updateTileByNew = function(checkNewValue){
            (checkNewValue) ? updateTiles ( vm.filterValue = 1 , checkNewValue) : console.log("not intro");
        };

        function updateTiles (id,style){
            var tiles = [];

            var index = vm.arrayFilter.map(function (option) {
                return option;
            }).indexOf(id);
            if(index == -1){
                vm.arrayFilter.push(id);
            }
            for(var i = 0; i < vm.arrayFilter.length; i++){
                console.log(vm.arrayFilter[i]);
                switch (vm.arrayFilter[i]){
                    case 1:

                }
            }


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
            $scope.shared = {};
            $scope.shared.tileId = tileId;
            $scope.shared.tileDetailTemplateUrl = baseSettings.staticUrl + 'app/tiles/templates/tileDetails.html'
        };

    }
}());
