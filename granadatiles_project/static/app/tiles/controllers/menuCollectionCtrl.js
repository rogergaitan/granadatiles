(function() {
    'use strict';

    angular
        .module('app.tiles')
        .controller('menuCollectionCtrl', ['baseSettings',
            'collectionsSvc',
            menuCollectionCtrl
        ]);

    function menuCollectionCtrl(baseSettings, collectionsSvc) {
        var vm = this;

        vm.labels = baseSettings.labels;
        vm.navigation = baseSettings.navigation;

        collectionsSvc.getMenuCollections().then(function(response) {
            vm.menuCollections = response.data;
        });
    }
}());