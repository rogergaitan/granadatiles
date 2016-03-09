(function () {
    'use strict';

    angular
        .module('app.cart')
        .controller('checkoutCtrl', checkoutCtrl);

    checkoutCtrl.$inject = ['pageSettings', 'cartSvc', 'checkoutSvc'];

    function checkoutCtrl(pageSettings, cartSvc, checkoutSvc) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;

        cartSvc.getCartTiles().then(function (response) {
            vm.tiles = response.data;
        });
    }
})();
