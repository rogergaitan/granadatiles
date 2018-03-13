(function () {
    'use strict';

    angular
        .module('app.core')
        .controller('confirmModalCtrl', confirmModalCtrl);

    confirmModalCtrl.$inject = ['baseSettings', '$modalInstance', 'initData'];

    function confirmModalCtrl(baseSettings, $modalInstance, initData) {
        /* jshint validthis:true */
        var vm = this;

        vm.labels = baseSettings.labels

        vm.message = initData.message;
        
        vm.ok = function () {
            $modalInstance.close();
        }

        vm.cancel = function () {
            $modalInstance.dismiss();
        }
    }
})();
