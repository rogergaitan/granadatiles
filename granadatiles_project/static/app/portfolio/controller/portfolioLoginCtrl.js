(function () {
    'use strict';

    angular
        .module('app.portfolio')
        .controller('portfolioLoginCtrl', portfolioLoginCtrl);

    portfolioLoginCtrl.$inject = ['pageSettings'];

    function portfolioLoginCtrl(pageSettings) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;

    }
})();
