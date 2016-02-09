(function() {
    'use strict';

    angular
        .module('app.tiles')
        .controller('menuCollectionCtrl', ['baseSettings',
            'collectionsSvc',
            'flatPagesSvc',
            menuCollectionCtrl
        ]);

    function menuCollectionCtrl(baseSettings, collectionsSvc, flatPagesSvc) {
        var vm = this;

        vm.labels = baseSettings.labels;
        vm.navigation = baseSettings.navigation;

        collectionsSvc.getMenuCollections().then(function(response) {
            vm.menuCollections = response.data;
        });

        flatPagesSvc.getFlatPagesMenu(1).then(function (response) {
            vm.flatPages = response.data;
        });
    }
}());