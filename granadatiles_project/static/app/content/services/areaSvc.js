(function () {
    "use strict";

    angular
        .module("app.content")
        .factory("areaSvc", ['pageSettings', areaSvc]);


    function areaSvc(pageSettingsSvc) {
        console.log(pageSettingsSvc.settings.areaId);
        return {
            getArea: {}
        }
    }
})();