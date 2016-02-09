(function () {
    'use strict';

    angular
        .module('app.content')
        .controller('coverCtrl',
        [
            'baseSettings',
            'pageSettings',
            'sectionSvc',
            'flatPagesSvc',
            coverCtrl
        ]);

    function coverCtrl(baseSettings, pageSettings, sectionSvc, flatPagesSvc) {
        var vm = this;

        if (pageSettings.sectionId != 0) {
            sectionSvc.getCover(pageSettings.sectionId).then(function (response) {
                vm.cover = response.data;
            });
        } else
        {
            if (pageSettings.flatPageTitle)
            {
                flatPagesSvc.getFlatPageCover(pageSettings.flatPageTitle).then(function (response) {
                    vm.cover = response.data;
                })
            }
        }

        vm.labels = baseSettings.labels;
    }
}());