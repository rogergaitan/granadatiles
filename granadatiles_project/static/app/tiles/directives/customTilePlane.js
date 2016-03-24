(function () {
    'use strict';

    angular
        .module('app')
        .directive('customTilePlane', customTilePlane);

    customTilePlane.$inject = ['baseSettings'];

    function customTilePlane(baseSettings) {
        // Usage:
        //     <custom-tile-plane></custom-tile-plane>
        // Creates:
        // 
        var directive = {
            link: link,
            restrict: 'E',
            scope: {
                plane: '=',
                colorGroups: '='
            },
            templateUrl: baseSettings.staticUrl + 'app/tiles/directives/customTilePlane.html',
            controller: ['customTilesSvc', '$scope', customTilePlaneCtrl]
        };
        return directive;

        function link(scope, element, attrs) {
            scope.$watch('tilePlane', function (oldValue, newValue) {
                if (oldValue != newValue) {
                    for (var i = 0; i < scope.colorGroups.length; i++) {
                        var path = element.find('[id="' + scope.colorGroups[i].group + '"]');
                        for (var j = 0; j < path.children().length; j++) {
                            var children = angular.element(path.children()[j])
                            children.attr('fill', scope.colorGroups[i].color.hexadecimalCode);
                            children.css('fill', scope.colorGroups[i].color.hexadecimalCode);
                        }
                        path.attr('fill', scope.colorGroups[i].color.hexadecimalCode);
                        path.css('fill', scope.colorGroups[i].color.hexadecimalCode);
                    }
                }
            });
        }

        function customTilePlaneCtrl(customTilesSvc, $scope) {
            customTilesSvc.getTilePlane($scope.plane).then(function (response) {
                $scope.tilePlane = response.data;
            });
        }
    }

})();