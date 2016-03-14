(function () {
    'use strict';

    angular
        .module('app')
        .controller('shareModalCtrl', shareModalCtrl);

    shareModalCtrl.$inject = ['shareUrl', '$modalInstance'];

    function shareModalCtrl(shareUrl, $modalInstance) {
        /* jshint validthis:true */
        var vm = this;
        vm.url = shareUrl;

        vm.close = function () {
            $modalInstance.close();
        }
    }
})();
