(function () {
    'use strict';

    angular
        .module('app')
        .controller('createLayoutCtrl', createLayoutCtrl);

    createLayoutCtrl.$inject = ['pageSettings', 'baseSettings', 'sectionSvc', 'portfolioSvc', 'sharePageSvc', 'authenticationSvc'];

    function createLayoutCtrl(pageSettings, baseSettings, sectionSvc, portfolioSvc, sharePageSvc, authenticationSvc) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.navigation = pageSettings.navigation;
        vm.logoutUrl = pageSettings.logoutUrl;
        vm.loggedUser = pageSettings.loggedUser
        vm.createLayout = true;

        vm.portfolioAsideMenuTemplateURl = baseSettings.staticUrl + 'app/portfolio/templates/portfolioAsideMenu.html'

        sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
            vm.section = response.data;
        });

        vm.myAccount = function () {
            authenticationSvc.myAccountModal(vm.loggedUser)
        };
    }
})();
