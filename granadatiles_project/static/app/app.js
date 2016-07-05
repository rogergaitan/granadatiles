(function() {
    'use strict';
    
    angular
        .module('app', ['ngSanitize',
            'ngAnimate',
            'toastr',
            'ui.bootstrap',
            'mega-menu',
            'angular-loading-bar',
            '720kb.socialshare',
            'vcRecaptcha',
            'checklist-model',
            'infinite-scroll',
            'ang-drag-drop',


            'app.core',
            'app.content',
            'app.tiles',
            'app.galleries',
            'app.news',
            'app.portfolio',
            'app.cart'
        ]).config(['$provide', function ($provide) {
            $provide.decorator('$browser', ['$delegate', function ($delegate) {
                $delegate.onUrlChange = function () { };
                $delegate.url = function () { return "" };
                return $delegate;
            }]);
        }]);
}());