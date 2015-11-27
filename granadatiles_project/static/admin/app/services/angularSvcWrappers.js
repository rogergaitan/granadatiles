(function () {
    'use strict';

    angular
        .module('app')
        .service('angularSvcWrappers', angularSvcWrappers);


    function angularSvcWrappers() {
        this.$ = $;
        this.Chart = Chart;

    }
})();