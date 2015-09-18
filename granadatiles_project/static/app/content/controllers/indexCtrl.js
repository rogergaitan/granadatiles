(function() {
    'use strict';

    angular
        .module('app.content')
        .controller('indexCtrl', ['appSettings',
            'pageSettings',
            'areaSvc',
            'collectionsSvc',
            indexCtrl
        ]);

    function indexCtrl(appSettings, pageSettings, areaSvc, collectionsSvc) {
        var vm = this;
        collectionsSvc.getFeaturedCollections().then(function (response) {
            vm.collections = response.data;
        });
        vm.slogan = areaSvc.getArea(appSettings.areas.SLOGAN).description;

        vm.labels = pageSettings.labels;
    }
}());