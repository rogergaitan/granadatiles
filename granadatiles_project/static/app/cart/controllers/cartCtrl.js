(function () {
    'use strict';

    angular
        .module('app.cart')
        .controller('cartCtrl', cartCtrl);

    cartCtrl.$inject = ['pageSettings', 'cartSvc'];

    function cartCtrl(pageSettings, cartSvc) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.navigation = pageSettings.navigation;
        vm.subTotal = 0;
        vm.total = 0;
        vm.sampleSubTotal = 0;
        vm.sampleTotal = 0;
        vm.quantityForSamples = [];

        cartSvc.getCartTiles().then(function (response) {
            vm.orders = response.data;
            for (var i = 0; i < vm.orders.length; i++) {
                vm.subTotal += vm.orders[i].subtotal;
            }
            vm.total = vm.subTotal;
        });

        cartSvc.getCartSamples().then(function (response) {
            vm.sampleOrders = response.data;
            for (var i = 0; i < vm.sampleOrders.length; i++) {
                vm.sampleSubTotal += vm.sampleOrders[i].subtotal;
            }
            vm.sampleTotal = vm.sampleSubTotal;
        });

        vm.updateSqFt = function (order) {
            cartSvc.updateTile({
                sqFt: order.sqFt,
                id: order.tile.id
            }).then(function (response) {
                var data = response.data;
                order.boxes = data.boxes;
                order.quantity = data.quantity;
                order.subtotal = data.subtotal;
            });
        };

        vm.removeTile = function (order) {
            cartSvc.removeTile(order.tile.id).then(function (response) {
                order.removed = true;
            });
        };

        vm.removeSample = function (sampleOrder) {
            cartSvc.removeSample(sampleOrder.tile.id).then(function (response) {
                sampleOrder.removed = true;
            });
        };

        for (var i = 1; i <= 10; i++) {
            vm.quantityForSamples.push(i);
        }

        vm.updateSampleQuantity = function (sampleOrder) {
            console.log(sampleOrder);
            //Update backEnd and total
        };

    }
})();
