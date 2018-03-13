(function() {
    'use strict';

    angular
        .module('app.content')
        .factory('areaSvc', 
            ['$http',
             'appSettings',
             areaSvc]);


    function areaSvc($http, appSettings) {

        return {
            getArea: getArea
        };

        function getArea(areaId) {
            return $http.get(appSettings.serverPath + 'areas/' + areaId);
        }

    }
})();