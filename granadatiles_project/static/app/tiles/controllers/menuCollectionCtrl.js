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
        /*Translations*/
        vm.browse = baseSettings.labels.browse;

        collectionsSvc.getMenuCollections().then(function(response) {
            vm.menuCollections = response.data;
        });
    }
}());