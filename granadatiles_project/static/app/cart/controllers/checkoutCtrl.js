(function () {
    'use strict';

    angular
        .module('app.cart')
        .controller('checkoutCtrl', checkoutCtrl);

    checkoutCtrl.$inject = ['pageSettings', 'cartSvc', 'checkoutSvc', 'customTilesSvc', '$q'];

    function checkoutCtrl(pageSettings, cartSvc, checkoutSvc, customTilesSvc, $q) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.navigation = pageSettings.navigation;
        vm.subTotal = 0;
        vm.total = 0;
        vm.activeStep = 1;

        var orders = cartSvc.getCartTiles();
        var sampleOrders = cartSvc.getCartSamples();
        var cartCustomizedTilesOrders = cartSvc.getCustomizedTiles();

        $q.all([orders, sampleOrders, cartCustomizedTilesOrders]).then(function (response) {
            vm.orders = response[0].data;
            vm.sampleOrders = response[1].data;
            vm.customizedOrders = response[2].data;

            for (var i = 0; i < vm.orders.length; i++) {
                vm.subTotal += vm.orders[i].subtotal;
            }
            for (var i = 0; i < vm.customizedOrders.length; i++) {
                vm.customizedOrders[i].tile.colors = customTilesSvc.getColorsUsed(vm.customizedOrders[i].groupColors);
                vm.customizedOrders[i].tile.inStock = false;
                vm.subTotal += vm.customizedOrders[i].subtotal;
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
