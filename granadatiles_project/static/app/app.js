﻿(function() {
    'use strict';
    
    angular
        .module('app', ['ngSanitize',
            'ngAnimate',
            'ui.bootstrap',
            'mega-menu',
            'angular-loading-bar',
            '720kb.socialshare',

            'app.core',
            'app.content',
            'app.tiles',
            'app.galleries',
            'app.news'
        ]);
}());