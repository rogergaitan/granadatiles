(function () {
    'use strict';

    angular
        .module('app')
        .factory('gtUtilsSvc', gtUtilsSvc);


    function gtUtilsSvc() {
        var service = {
            getQueryStringParameterByName: getQueryStringParameterByName
        };

        return service;

        function getQueryStringParameterByName(name) {
            name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
            var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
                results = regex.exec(location.search);
            return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
        }
    }
})();