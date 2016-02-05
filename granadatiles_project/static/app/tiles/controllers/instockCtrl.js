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

        sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
            vm.section = response.data;
        });

        


    }
})();
