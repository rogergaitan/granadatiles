(function() {
    'use strict';

    angular
        .module('app.content')
        .controller('coverCtrl', ['appSettings',
            'pageSettings',
            'sectionSvc',
            coverCtrl
        ]);

    function coverCtrl(appSettings, pageSettings, sectionSvc) {
        var vm = this;

        if (pageSettings.sectionId != 0) {
            sectionSvc.getCover(pageSettings.sectionId).then(function (response) {
                vm.cover = response.data;
            });
        }

        vm.labels = pageSettings.labels;
    }
}());