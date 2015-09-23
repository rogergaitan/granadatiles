(function() {
    'use strict';

    angular
        .module('app', ['ngSanitize',
            'ngAnimate',
            'angular-loading-bar',

            'app.core',
            'app.content',
            'app.tiles',
            'app.galleries',
            'app.news'
        ]);
}());