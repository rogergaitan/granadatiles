(function() {
    'use strict';
    
    angular
        .module('app', ['ngSanitize',
            'ngAnimate',
            'ui.bootstrap',
            'mega-menu',
            'angular-loading-bar',
            '720kb.socialshare',
            'vcRecaptcha',
            'checklist-model',

            'app.core',
            'app.content',
            'app.tiles',
            'app.galleries',
            'app.news',
            'app.portfolio'
        ]);
}());