(function () {
    'use strict';

    angular
        .module('app.tiles')
        .controller('tileModalCtrl',
                    ['installationPhotos',
                    '$modalInstance',
                    tileModalCtrl]);

    function tileModalCtrl(installationPhotos, $modalInstance) {
        var vm = this;

        console.log("intro");

        vm.installationPhotos = installationPhotos;

        vm.close = function () {
            $modalInstance.dismiss('cancel');
        };
    }
})();