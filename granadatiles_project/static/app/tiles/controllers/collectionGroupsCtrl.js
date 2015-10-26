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
            console.log(vm.tiles);
        });*/

        vm.tiles = collectionsSvc.getTiles();
        console.log(vm.tiles);

        vm.labels = pageSettings.labels;

        vm.subMenuCollapsed = true;

    }
}());
