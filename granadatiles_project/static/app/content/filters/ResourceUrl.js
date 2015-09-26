(function() {
    'use strict';

    angular.
    module('app.content')
        .filter('trustAsResourceUrl', ['$sce', function($sce) {
            return function(val) {
                return $sce.trustAsResourceUrl(val);
            };
        }])
}());