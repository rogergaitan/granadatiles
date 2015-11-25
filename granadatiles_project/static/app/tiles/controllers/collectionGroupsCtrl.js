(function () {
    'use strict';

    angular
        .module('app.tiles')
        .controller('collectionsGroupCtrl',
                    ['baseSettings',
                     'pageSettings',
                     'collectionsSvc',
                     collectionsGroupCtrl
        ]);

    function collectionsGroupCtrl(baseSettings ,pageSettings, collectionsSvc) {
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

        /*collectionsSvc.getTiles(pageSettings.groupId).then(function (response) {
            vm.tiles = response.data;
        });*/

        collectionsSvc.getSizes(pageSettings.groupId).then(function (response) {
            vm.sizes = response.data;
            vm.selectedSize = vm.sizes[0];
            //updateTiles(vm.sizes[0]);
        });

        collectionsSvc.getStyles(pageSettings.groupId).then(function (response) {
            vm.styles = response.data;
        });

        vm.tiles = collectionsSvc.getTiles(pageSettings.groupId);

        vm.labels = pageSettings.labels;

        vm.subMenuCollapsed = true;

        vm.setSize = function(size) {
            vm.selectedSize = size;
            //updateTiles(size);
        };

        function updateTiles(selectedSize){
            collectionsSvc.getArticlesFiltered(selectedSize).then(function (response){
                vm.tiles = response.data;
            });
        }

    }
}());
