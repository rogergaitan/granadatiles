(function () {
    'use strict';

    angular
        .module('app')
        .factory('gtUtilsSvc', ['$window', gtUtilsSvc]);


    function gtUtilsSvc($window) {
        var service = {
            getQueryStringParameterByName: getQueryStringParameterByName,
            addQueryStringParameter: addQueryStringParameter,
            removeQueryStringParameters: removeQueryStringParameters
        };

        return service;

        function getQueryStringParameterByName(name) {
            name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
            var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
                results = regex.exec(location.search);
            return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
        }

        function addQueryStringParameter(name, value) {
            var newurl = window.location.protocol + "//" + window.location.host + window.location.pathname + '?' + name + '=' + value;
            $window.history.pushState({ path: newurl }, '', newurl)
        }

        function removeQueryStringParameters() {
            var newurl = window.location.protocol + "//" + window.location.host + window.location.pathname;
            $window.history.pushState({ path: newurl }, '', newurl)
        }

    }
})();