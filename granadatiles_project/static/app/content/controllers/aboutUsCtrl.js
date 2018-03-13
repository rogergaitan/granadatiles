(function () {
    'use strict';

    angular
        .module('app.content')
        .controller('aboutUsCtrl', aboutUsCtrl);

    aboutUsCtrl.$inject = ['pageSettings', 'sectionSvc'];

    function aboutUsCtrl(pageSettings, sectionSvc) {
        /* jshint validthis:true */
        var vm = this;
       
        vm.labels = pageSettings.labels;

        sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
            vm.section = response.data;
        });
    }
})();
