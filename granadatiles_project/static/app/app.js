(function() {
    'use strict';
    
    angular
        .module('app', ['ngSanitize',
            'ui.bootstrap',
            'mega-menu',
            'ngAnimate',
            'angular-loading-bar',
            '720kb.socialshare',

            'app.core',
            'app.content',
            'app.tiles',
            'app.galleries',
            'app.news'
        ]);
}());