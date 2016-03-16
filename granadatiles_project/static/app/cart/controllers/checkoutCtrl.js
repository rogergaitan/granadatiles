(function () {
    'use strict';

    angular
        .module('app.cart')
        .controller('checkoutCtrl', checkoutCtrl);

    checkoutCtrl.$inject = ['pageSettings', 'cartSvc', 'checkoutSvc', '$q'];

    function checkoutCtrl(pageSettings, cartSvc, checkoutSvc, $q) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.navigation = pageSettings.navigation;
        vm.subTotal = 0;
        vm.total = 0;
        vm.activeStep = 1;

        var orders = cartSvc.getCartTiles();
        var sampleOrders = cartSvc.getCartSamples();

        $q.all([orders, sampleOrders]).then(function (response) {
            vm.orders = response[0].data;
            vm.sampleOrders = response[1].data;
            for (var i = 0; i < vm.orders.length; i++) {
                vm.subTotal += vm.orders[i].subtotal;
            }
            for (var i = 0; i < vm.sampleOrders.length; i++) {
                vm.subTotal += vm.sampleOrders[i].subtotal;
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
