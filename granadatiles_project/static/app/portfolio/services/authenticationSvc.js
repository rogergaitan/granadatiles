(function () {
    'use strict';

    angular
        .module('app.portfolio')
        .factory('authenticationSvc', authenticationSvc);

    authenticationSvc.$inject = ['baseSettings', '$http', '$modal'];

    function authenticationSvc(baseSettings, $http, $modal) {
        var service = {
            registerUser: registerUser,
            myAccountModal: myAccountModal
        };

        return service;

        function registerUser(data) {
            return $http.post('/en/portfolio/account/signup/', data)
        }

        function myAccountModal(user) {
            $modal.open({
                templateUrl: baseSettings.staticUrl + 'app/portfolio/templates/myAccount.html',
                controller: 'myAccountCtrl',
                controllerAs: 'vm',
                windowClass: 'my-account-modal',
                resolve: {
                    initData: function () {
                        return {
                            user:user
                        }
                    }
                }
            })
        }
    }
})();