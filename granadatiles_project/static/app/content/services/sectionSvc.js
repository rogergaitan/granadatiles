(function () {
    "use strict";

    angular
        .module("app.content")
        .factory("sectionSvc",
                ['pageSettings',
                  sectionSvc]);


    function sectionSvc(pageSettingsSvc) {

        return {
            getSection: getSection
        };

        var mockSection = {
        };

        function getSection(sectionId) {
            return mockSection;
        }
    }
})();