﻿(function () {
    'use strict';

    angular
        .module('app')
        .controller('galleryModalCtrl',
                    ['gallery',
                     '$modalInstance',
                     galleryModalCtrl]);

    function galleryModalCtrl(gallery, $modalInstance) {
        var vm = this;

        vm.gallery = gallery

        vm.close = function () {
            $modalInstance.dismiss('cancel');
        };
    }
})();
