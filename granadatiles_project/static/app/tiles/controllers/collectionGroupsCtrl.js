(function () {
    'use strict';

    angular
        .module('app.tiles')
        .controller('collectionsGroupCtrl', ['pageSettings', 'collectionsSvc', collectionsGroupCtrl
        ]);

    function collectionsGroupCtrl(pageSettings, collectionsSvc) {
        var vm = this;

        collectionsSvc.getCollection(pageSettings.collectionId).then(function (response) {
            vm.collection = response.data;
        });

        collectionsSvc.getCollectionGroups(pageSettings.collectionId).then(function (response) {
            vm.collectionGroups = response.data;
        });

        vm.labels = pageSettings.labels;

    }
}());
