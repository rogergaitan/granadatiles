(function () {
    'use strict';

    angular
        .module('app.portfolio')
        .controller('layoutsCtrl', layoutsCtrl);

    layoutsCtrl.$inject = ['pageSettings', 'sectionSvc', 'baseSettings', 'portfolioSvc', 'sharePageSvc'];

    function layoutsCtrl(pageSettings, sectionSvc, baseSettings, portfolioSvc, sharePageSvc) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.navigation = pageSettings.navigation;
        vm.logoutUrl = pageSettings.logoutUrl;
        vm.loggedUser = pageSettings.loggedUser

        vm.portfolioAsideMenuTemplateURl = baseSettings.staticUrl + 'app/portfolio/templates/portfolioAsideMenu.html'

        sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
            vm.section = response.data;
        });

    }
})();
