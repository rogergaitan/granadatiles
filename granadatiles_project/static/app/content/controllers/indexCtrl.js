(function() {
    'use strict';

    angular
        .module('app.content')
        .controller('indexCtrl', ['appSettings',
            'pageSettings',
            'areaSvc',
            'collectionsSvc',
            'mainNavigationSvc',
            indexCtrl
        ]);

    function indexCtrl(appSettings, pageSettings, areaSvc, collectionsSvc, mainNavigationSvc) {
        var vm = this;
        collectionsSvc.getFeaturedCollections().then(function (response) {
            vm.collections = response.data;
        });

        vm.labels = pageSettings.labels;

        mainNavigationSvc.getmainNavigation().then(function (response) {
            vm.navigation = response.data;
        });
    }
}());