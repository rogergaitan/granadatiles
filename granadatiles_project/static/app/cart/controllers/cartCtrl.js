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

    }
})();
