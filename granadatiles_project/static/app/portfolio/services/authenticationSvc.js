(function () {
    'use strict';

    angular
        .module('app.portfolio')
        .factory('authenticationSvc', authenticationSvc);

    authenticationSvc.$inject = ['$http'];

    function authenticationSvc($http) {
        var service = {
            registerUser: registerUser
        };

        return service;

        function registerUser(data) {
            return $http.post('/en/portfolio/account/signup/', data)
        }
    }
})();