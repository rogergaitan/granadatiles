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

        vm.collectionSubMenuTemplateUrl = baseSettings.staticUrl + 'app/tiles/templates/collectionSubMenu.html';

        collectionsSvc.getCollection(pageSettings.collectionId).then(function (response) {
            vm.collection = response.data;
        });

        collectionsSvc.getCollectionGroups(pageSettings.collectionId).then(function (response) {
            vm.collectionGroups = response.data;
        });

        collectionsSvc.getFilteredMenuCollection(pageSettings.collectionId).then(function (response) {
            vm.filteredMenuCollection = response.data;
        });

        vm.labels = pageSettings.labels;

        vm.subMenuCollapsed = true;

    }
}());
