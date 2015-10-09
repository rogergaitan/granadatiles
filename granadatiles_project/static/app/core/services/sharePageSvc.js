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

        function shareModal() {
            $modal.open({
                templateUrl: baseSettings.staticUrl + 'app/core/templates/sharePageModal.html'
            });
        }
    }
})();