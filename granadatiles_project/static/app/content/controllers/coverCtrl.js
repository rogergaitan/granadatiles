(function () {
    "use strict";

    angular
        .module("app.content")
        .controller('coverCtrl',
                    ['appSettings',
                    'pageSettings',
                    'sectionSvc',
                    coverCtrl]);

    function coverCtrl(appSettings, pageSettings, sectionSvc) {
        var vm = this;

        vm.cover = sectionSvc.getCover(pageSettings.sectionId);
    }
})();