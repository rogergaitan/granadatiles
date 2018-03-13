(function () {
    'use strict';

    angular
        .module('app.core')
        .factory('gtDialogsSvc', gtDialogs);

    gtDialogs.$inject = ['baseSettings', '$modal'];

    function gtDialogs(baseSettings, $modal) {
        var service = {
            confirmModal: confirmModal
        };

        return service;

        function confirmModal(message) {
            return $modal.open({
                templateUrl: baseSettings.staticUrl + 'app/core/templates/confirmModal.html',
                controller: 'confirmModalCtrl',
                controllerAs: 'vm',
                resolve: {
                    initData: function () {
                        return {
                            message: message
                        };
                    }
                }
            });
        }
    }
})();