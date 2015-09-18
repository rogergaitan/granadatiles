(function() {
    'use strict';

    angular
        .module('app.content')
        .factory('areaSvc', ['pageSettings', areaSvc]);


    function areaSvc(pageSettingsSvc) {

        return {
            getArea: getArea
        };


        function getArea(areaId) {
            return getMockArea();
        }

        //TODO API /api/area/:id
        function getMockArea() {
            return {
                description: '<h2 class="heading-sec">Get inspired by Residential and Commercial installation photos</h2><h3 class="slogan">then choose from in stock and custom tiles.</h3>',
                id: 1
            };
        }

    }
})();