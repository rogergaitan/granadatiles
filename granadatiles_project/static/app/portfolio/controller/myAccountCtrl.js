(function () {
    'use strict';

    angular
        .module('app')
        .controller('myAccountCtrl', myAccountCtrl);

    myAccountCtrl.$inject = ['pageSettings']; 

    function myAccountCtrl(pageSettings) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;

    }
})();
