(function () {
    'use strict';

    angular
        .module('app.core')
        .filter('unsafe', function ($sce) { return $sce.trustAsHtml; });
    
})();