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

        cartSvc.getCartTiles().then(function (response) {
            vm.orders = response.data;
            for (var i = 0; i < vm.orders.length; i++) {
                vm.subTotal += vm.orders[i].subtotal;
            }
            vm.total = vm.subTotal;
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
        }
    }
})();
