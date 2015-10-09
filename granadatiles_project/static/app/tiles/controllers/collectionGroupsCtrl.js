(function () {
    'use strict';

    angular
        .module('app.tiles')
        .controller('collectionsGroupCtrl', ['pageSettings',
            'collectionsSvc',
            collectionsGroupCtrl
        ]);

    function collectionsGroupCtrl(pageSettings, collectionsSvc) {
        var vm = this;

        collectionsSvc.getCollectionGroups(pageSettings.collectionId).then(function (response) {
            vm.collectionGroups = response.data;
        });

        vm.title = 'Echo Tile Collection Interactive Catalog ';

        vm.description = '<p>The Echo Tile Collection revitalizes an art form that developed in France in the mid-1800s\ ' +
                        'and quickly spread around the world. Unlike ceramic tiles, which are usually glazed and ?red,\ ' +
                        'decorative cement tiles are made by ?rst pouring a mixture of cement and color pigment into\ ' +
                        'separate compartments in a metal mold.</p>';

    }
}());
