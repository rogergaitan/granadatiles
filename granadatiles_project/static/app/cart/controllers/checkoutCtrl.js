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
        vm.navigation = pageSettings.navigation;
        vm.subTotal = 0;
        vm.total = 0;
        vm.activeStep = 1;

        cartSvc.getCartTiles().then(function (response) {
            vm.orders = response.data;
            for (var i = 0; i < vm.orders.length; i++) {
                vm.subTotal += vm.orders[i].subtotal;
            }
            vm.total = vm.subTotal;
        });

        vm.navigateToStep = function (step) {
            vm.activeStep = step;
        };

        vm.navigateToNextStep = function () {
            if (vm.activeStep != 3)
                vm.activeStep++;
        };

        vm.printOrder = function () {
            print();
        }
    }
})();
