(function () {
    'use strict';

    angular
        .module('app.core')
        .factory('addLanguage',
                ['pageSettings',
                 '$q',
                  addLanguage])
        .config(['$httpProvider',
                 function ($httpProvider) {
                     $httpProvider.interceptors.push('addLanguage');
                 }]);


    function addLanguage(pageSettings, $q) {

        function request(config) {
            config.headers['X-Language-Code'] = pageSettings.language;
            return $q.when(config);
        };

        return {
            request: request
        }
    };


}());