(function () {
    'use strict';

    angular
        .module('app.core')
        .factory('sharePageSvc', sharePageSvc);

    sharePageSvc.$inject = ['baseSettings', '$modal'];

    function sharePageSvc(baseSettings, $modal) {

        return {
            shareModal: shareModal
        };

        function shareModal(url) {
            $modal.open({
                templateUrl: baseSettings.staticUrl + 'app/core/templates/sharePageModal.html',
                controller: 'shareModalCtrl',
                controllerAs: 'vm',
                resolve: {
                    shareUrl: function () {
                        return url;
                    }
                }
            });
        }
    }
})();