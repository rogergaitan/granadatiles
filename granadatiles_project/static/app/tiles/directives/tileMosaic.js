(function() {
    'use strict';

    angular
        .module('app.tiles')
        .directive('tileMosaic', tileMosaic);
    tileMosaic.$inject = ['baseSettings', '$window'];
    
    function tileMosaic(baseSettings, $window) {
        // Usage:
        //     <tile-mosaic></tile-mosaic>
        // Creates:
        // 
        var directive = {
            link: link,
            restrict: 'E',
            scope: {
                tile: '=',
                repeatHorinzotal: '=',
                repeatVertical: '=',
                noBorders: '=',
            },
            templateUrl: baseSettings.staticUrl + 'app/tiles/directives/tileMosaic.html'
        };
        return directive;

        function link(scope, element, attrs) {
        }
    }

})();