(function () {
    'use strict';

    angular
        .module('app')
        .controller('shareModalCtrl', shareModalCtrl);

    shareModalCtrl.$inject = ['shareUrl', 'baseSettings', '$modalInstance'];

    function shareModalCtrl(shareUrl, baseSettings, $modalInstance) {
        /* jshint validthis:true */
        var vm = this;
        vm.url = shareUrl;
        vm.labels = baseSettings.labels;

        vm.close = function () {
            $modalInstance.close();
        }
    }
})();
