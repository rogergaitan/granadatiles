(function () {
    "use strict";
    angular
        .module("app.core", [])
        .constant("appSettings",
        {
            serverPath: "/api/"
        });
})();