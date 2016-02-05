(function () {
    'use strict';

    angular
        .module('app.tiles')
        .controller('instockCtrl', instockCtrl);

    instockCtrl.$inject = ['pageSettings', 'instockSvc', 'sectionSvc'];

    function instockCtrl(pageSettings, instockSvc, sectionSvc) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.navigation = pageSettings.navigation;
        vm.isSample = false;

        if (pageSettings.samples)
            vm.isSample = true;

        sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
            vm.section = response.data;
        });

        


    }
})();
