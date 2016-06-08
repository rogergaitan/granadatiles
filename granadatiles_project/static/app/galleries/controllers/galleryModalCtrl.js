(function () {
    'use strict';

    angular
        .module('app.galleries')
        .controller('galleryModalCtrl',
                    ['gallery',
                     'pageSettings',
                     '$modalInstance',
                     galleryModalCtrl]);

    function galleryModalCtrl(gallery, pageSettings, $modalInstance) {
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.gallery = gallery

        vm.close = function () {
            $modalInstance.dismiss('cancel');
        };
    }
})();
