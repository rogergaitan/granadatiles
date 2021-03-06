(function () {
    'use strict';

    angular
        .module('app.tiles')
        .controller('collectionsGroupsCtrl',
                    ['baseSettings',
                     'pageSettings',
                     'collectionsSvc',
                     'flatPagesSvc',
                     '$modal',
                     collectionsGroupsCtrl
                    ]);

    function collectionsGroupsCtrl(baseSettings,
                                  pageSettings,
                                  collectionsSvc,
                                  flatPagesSvc,
                                  $modal) {
        var vm = this;

        vm.labels = pageSettings.labels;

        vm.subMenuCollapsed = true;

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
}());
