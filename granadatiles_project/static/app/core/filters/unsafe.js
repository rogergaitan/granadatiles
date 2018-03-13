(function () {
    'use strict';

    angular
        .module('app.core')
        .filter('unsafe', ['$sce', function ($sce) { return $sce.trustAsHtml; }]);
    
})();