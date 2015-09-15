(function() {
    'use strict';

    angular.
    module('app.content')
        .directive('imgPreload', ['$rootScope',
            function($rootScope) {
                return {
                    restrict: 'A',
                    scope: {
                        ngSrc: '@'
                    },
                    link: function(scope, element, attrs) {
                        element.on('load', function() {
                            element.parent().find('#gt-cover-spinner').remove();
                            element.addClass('in');
                        }).on('error', function() {
                            //
                        });

                        scope.$watch('ngSrc', function(newVal) {
                            element.parent().append('<div id="gt-cover-spinner"><i class="fa fa-spinner fa-5x fa-spin"></i></div>');
                            element.removeClass('in');
                        });
                    }
                };
            }
        ]);
}());