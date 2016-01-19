(function () {
    'use strict';

    angular
        .module('app.core')
        .directive('fadeIn', fadeIn);

    fadeIn.$inject = ['$timeout'];

    function fadeIn($timeout) {

        var directive = {
            link: link,
            restrict: 'A'
        };
        return directive;

        function link(scope, element, attrs) {
            element.on("load", function () {
                $timeout(function () {
                    element.removeClass("ng-hide-fade");
                    element.addClass("ng-show");
                }, 100);
            });
            attrs.$observe("ngSrc", function () {
                element.removeClass("ng-show");
                element.addClass("ng-hide-fade");
            });
        }
    }

})();