(function () {
    "use strict";

    angular
        .module("app.content")
        .factory("areaSvc", ['pageSettings', areaSvc]);


    function areaSvc(pageSettingsSvc) {

        return {
            getArea: getArea
        };


        function getArea(areaId) {
            return getMockArea();
        }

        function getMockArea() {
            return  {
                description: '<h1>Get inspired by Residential and Commercial installation photos</h1><h3>then choose from in stock and custom tiles.</h3>'
            };
        }

    }
})();