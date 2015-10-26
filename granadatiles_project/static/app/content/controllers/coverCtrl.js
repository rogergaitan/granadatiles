(function () {
    'use strict';

    angular
        .module('app.content')
        .controller('coverCtrl',
        [
            'baseSettings',
            'pageSettings',
            'sectionSvc',
            coverCtrl
        ]);

    function coverCtrl(baseSettings, pageSettings, sectionSvc) {
        var vm = this;

        if (pageSettings.sectionId != 0) {
            sectionSvc.getCover(pageSettings.sectionId).then(function (response) {
                vm.cover = response.data;
            });
        }

        vm.labels = baseSettings.labels;
    }
}());