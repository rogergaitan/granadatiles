(function () {
    'use strict';

    angular.module('app', [
        // Angular modules
        //'ngAnimate',
        //'ngRoute'

        'app.core'
    ]).config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('[[').endSymbol(']]');
    });
})();
