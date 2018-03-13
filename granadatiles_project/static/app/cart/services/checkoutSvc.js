(function () {
    'use strict';

    angular
        .module('app.cart')
        .factory('checkoutSvc', checkoutSvc);

    checkoutSvc.$inject = ['$http', 'appSettings'];

    function checkoutSvc($http, appSettings) {
        var service = {
            getData: getData
        };

        return service;

        function getData() { }
    }
})();