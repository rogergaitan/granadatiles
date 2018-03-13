(function () {
    'use strict';

    angular
        .module('app.cart')
        .controller('cartMenuCtrl', cartMenuCtrl);

    cartMenuCtrl.$inject = ['cartSvc', 'baseSettings']; 

    function cartMenuCtrl(cartSvc, baseSettings) {
        /* jshint validthis:true */
        var vm = this;

        vm.labels = baseSettings.labels;
        vm.navigation = baseSettings.navigation;

        cartSvc.getCartTilesCount().then(function (response) {
            cartSvc.setCartCount(response.data.count);
            vm.cart = cartSvc.getCart();
        });
    }
})();
