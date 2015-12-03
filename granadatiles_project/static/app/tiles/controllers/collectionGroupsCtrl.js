(function () {
    'use strict';

    angular
        .module('app.tiles')
        .controller('collectionsGroupCtrl',
                    ['baseSettings',
                     'pageSettings',
                     'collectionsSvc',
                     '$modal',
                     collectionsGroupCtrl
        ]);

    function collectionsGroupCtrl(baseSettings ,pageSettings, collectionsSvc, $modal) {
        var vm = this;

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

        collectionsSvc.getTiles(pageSettings.groupId).then(function (response) {
            vm.tiles = response.data;
        });

        //vm.tiles = collectionsSvc.getTiles(pageSettings.groupId);

        /*collectionsSvc.getSizes(pageSettings.groupId).then(function (response) {
            vm.sizes = response.data;
            //vm.selectedSize = vm.sizes[0];
        });*/

        collectionsSvc.getStyles(pageSettings.groupId).then(function (response) {
            vm.styles = response.data;
            vm.selectedStyle = vm.styles[0];
            //updateTilesByStyle(vm.styles[0].name);
        });

        vm.labels = pageSettings.labels;

        vm.subMenuCollapsed = true;

        vm.setSize = function(size) {
            vm.selectedSize = size;
        };

        vm.setStyle = function(style) {
            vm.selectedStyle = style;
            updateTilesByStyle(style.name);
        };

        vm.setTile = function(index, tileId){
            collectionsSvc.getMainTile(tileId).then(function (response){
                vm.main = response.data;
                updateMain(index, vm.main);
            });

            var arrayTiles = [];
            for ( var i = 0; i < vm.tiles[index].tiles.length;i++ ){
                if(vm.tiles[index].tiles[i].id != tileId){
                    arrayTiles.push(vm.tiles[index].tiles[i])
                }
            }
            arrayTiles.push({
                'id':vm.tiles[index].main.id,
                'name':vm.tiles[index].main.name,
                'image':vm.tiles[index].main.image
                //'sizes':vm.tiles[index].main.sizes
            });
            vm.tiles[index].tiles = arrayTiles;

        };
        function updateMain(index, main){
            var setMain = [];
            setMain.push({
                'id':main.id,
                'name':main.name,
                'mosaic':main.mosaic,
                'image':main.image,
                'sizes':main.sizes
            });
            vm.tiles[index].main = setMain[0];
        }

        function updateTilesByStyle(selectedStyle){
            collectionsSvc.getTileFilteredByStyle(pageSettings.groupId, selectedStyle).then(function (response){
                vm.tiles = response.data;
            });
        }

        vm.showInstallationPhoto = function(tileId) {
            console.log(tileId);
            $modal.open({
                templateUrl: baseSettings.staticUrl + 'app/tiles/templates/tileModal.html',
                controller: 'tileModalCtrl',
                controllerAs: 'vm',
                size:'lg',
                resolve:{
                    installationPhotos: function () {
                        return collectionsSvc.getInstallationPhoto(tileId).then(function (response) {
                            return response.data;
                        });
                    }
                }
            })
        };

    }
}());
