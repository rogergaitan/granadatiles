(function () {
    'use strict';

    angular
        .module('app.content')
        .controller('collectionContentCtrl', collectionContentCtrl);

    collectionContentCtrl.$inject = ['baseSettings',
                                    'pageSettings',
                                    'flatPagesSvc',
                                    'collectionsSvc',
                                    '$modal'];

    function collectionContentCtrl(baseSettings, pageSettings, flatPagesSvc, collectionsSvc, $modal) {
        /* jshint validthis:true */
        var vm = this;

        vm.navigation = pageSettings.navigation;
        vm.labels = pageSettings.labels;
        vm.collectionId = pageSettings.collectionId;

        vm.subMenuCollapsed = true;

        vm.collectionAsideNavigationTemplateUrl = baseSettings.staticUrl + 'app/tiles/templates/collectionAsideNavigation.html';

        flatPagesSvc.getCollectionContent(pageSettings.flatPageTitle).then(function (response) {
            vm.section = response.data;

            collectionsSvc.getCollection(vm.section.collectionId).then(function (response) {
                vm.collection = response.data;
            });

            collectionsSvc.getCollectionGroups(vm.section.collectionId).then(function (response) {
                vm.collectionGroups = response.data;
            });

            collectionsSvc.getFilteredMenuCollection(vm.section.collectionId).then(function (response) {
                vm.filteredMenuCollection = response.data;
            });

            flatPagesSvc.getCollectionContentMenu(vm.section.collectionId).then(function (response) {
                vm.collectionContent = response.data;
            });
        });

        vm.showCollectionGallery = function () {
            $modal.open({
                templateUrl: baseSettings.staticUrl + 'app/tiles/templates/tileModal.html',
                controller: 'tileModalCtrl',
                controllerAs: 'vm',
                size: 'lg',
                resolve: {
                    installationPhotos: function () {
                        return collectionsSvc.getCollectionGallery(vm.section.collectionId).then(function (response) {
                            return response.data;
                        });
                    }
                }
            })
        };
    }
})();
