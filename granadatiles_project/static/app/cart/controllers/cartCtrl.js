(function () {
    'use strict';

    angular
        .module('app.cart')
        .controller('cartCtrl', cartCtrl);

    cartCtrl.$inject = ['pageSettings', 'cartSvc', '$q', 'customTilesSvc'];

    function cartCtrl(pageSettings, cartSvc, $q, customTilesSvc) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.navigation = pageSettings.navigation;
        vm.subTotal = 0;
        vm.total = 0;
        vm.sampleSubTotal = 0;
        vm.sampleTotal = 0;
        vm.quantityForSamples = [];

        var cartTiles = cartSvc.getCartTiles();
        var cartCustomizedTiles = cartSvc.getCustomizedTiles();

        $q.all([cartTiles, cartCustomizedTiles]).then(function (response) {
            vm.orders = response[0].data;
            vm.customizedOrders = response[1].data;

            for (var i = 0; i < vm.orders.length; i++) {
                vm.subTotal += vm.orders[i].subtotal;
            }
            for (var i = 0; i < vm.customizedOrders.length; i++) {
                vm.customizedOrders[i].tile.colors = customTilesSvc.getColorsUsed(vm.customizedOrders[i].groupColors);
                vm.customizedOrders[i].tile.inStock = false;
                vm.subTotal += vm.customizedOrders[i].subtotal;
            }
            vm.total = vm.subTotal;
        })

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
                id: order.id
            }).then(function (response) {
                var data = response.data;
                order.boxes = data.boxes;
                order.quantity = data.quantity;
                order.subtotal = data.subtotal;
            });
        };

        vm.removeTile = function (order) {
            cartSvc.removeTile(order.id).then(function (response) {
                order.removed = true;
                var cart = cartSvc.getCart();
                cartSvc.setCartCount(cart.count - 1);
            });
        };

        vm.updateCustomizedTileSqFt = function (order) {
            cartSvc.updateCustomizedTile({
                sqFt: order.sqFt,
                id: order.id
            }).then(function (response) {
                var data = response.data;
                order.boxes = data.boxes;
                order.quantity = data.quantity;
                order.subtotal = data.subtotal;
            });
        }

        vm.removeCustomizedTile = function (order) {
            cartSvc.removeCusomizedTile(order.id).then(function (response) {
                order.removed = true;
                var cart = cartSvc.getCart();
                cartSvc.setCartCount(cart.count - 1);
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
            var sample = {
                id: sampleOrder.tile.id,
                quantity: parseInt(sampleOrder.selectedQuantity)
            }
            cartSvc.updateSample(sample).then(function (response) {
                
            });
        };

    }
})();
