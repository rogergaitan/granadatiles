(function() {
    'use strict';

    angular
        .module('app.content')
        .factory('sectionSvc', ['$http','appSettings', sectionSvc]);


    function sectionSvc($http, appSettings) {

        return {
            getSection: getSection,
            getCover: getCover
        };

        function getCover(sectionId) {
            return $http.get(appSettings.serverPath + 'sections/' + sectionId + '/cover');
        }

        function getSection(sectionId) {
            return $http.get(appSettings.serverPath + 'sections/' + sectionId );
        }


    }
})();