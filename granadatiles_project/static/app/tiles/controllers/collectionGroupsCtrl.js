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
            console.log(vm.tiles);
        });

        //vm.tiles = collectionsSvc.getTiles(pageSettings.groupId);

        collectionsSvc.getSizes(pageSettings.groupId).then(function (response) {
            vm.sizes = response.data;
            //vm.selectedSize = vm.sizes[0];
        });

        collectionsSvc.getStyles(pageSettings.groupId).then(function (response) {
            vm.styles = response.data;
            vm.selectedStyle = vm.styles[0];
        });



        vm.labels = pageSettings.labels;

        vm.subMenuCollapsed = true;

        vm.setSize = function(size) {
            vm.selectedSize = size;
        };

        vm.setStyle = function(style) {
            vm.selectedStyle = style;
        };

        vm.setTile = function(tileId){
            console.log(tileId);
            collectionsSvc.getMainTile(tileId).then(function (response){
                vm.main = response.data;
                console.log(vm.main);
            });
        };

        vm.showInstallationPhoto = function(tileId) {
            $modal.open({
                templateUrl: baseSettings.staticUrl + 'app/tiles/templates/tileModal.html',
                controller: 'tileModalCtrl',
                controllerAs: 'vm',
                size:'lg',
                resolve:{
                    installationPhotos: function () {
                        return collectionsSvc.getInstallationPhoto(tileId).then(function (response) {
                            //console.log(response.data);
                            return response.data;
                        });
                    }
                }
            })
        };

    }
}());
