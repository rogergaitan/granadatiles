(function () {
    'use strict';

    angular
        .module('app.core')
        .filter('nextInt', nextInt);
    
    function nextInt() {
        return nextIntFilter;

        function nextIntFilter(input) {
            return Math.ceil(input);
        }
    }
})();