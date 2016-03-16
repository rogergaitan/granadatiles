(function () {
    'use strict';

    angular
        .module('app.core')
        .filter('range', range);
    
    function range() {
        return rangeFilter;

        function rangeFilter(input, total) {
            if (!total)
                total = 1;
            total = parseInt(total);

            for (var i = 0; i < total; i++) {
                input.push(i);
            }

            return input;
        }
    }
})();