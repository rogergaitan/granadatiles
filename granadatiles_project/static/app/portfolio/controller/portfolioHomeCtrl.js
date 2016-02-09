(function () {
    'use strict';

    angular
        .module('app.portfolio')
        .controller('portfolioHomeCtrl', portfolioHomeCtrl);

    portfolioHomeCtrl.$inject = ['pageSettings', 'sectionSvc', 'baseSettings'];

    function portfolioHomeCtrl(pageSettings, sectionSvc, baseSettings) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.logoutUrl = pageSettings.logoutUrl;
        vm.loggedUser = pageSettings.loggedUser;

        vm.portfolioAsideMenuTemplateURl = baseSettings.staticUrl + 'app/portfolio/templates/portfolioAsideMenu.html'
        

        vm.user = {
            name: 'Melanie'
        }

        sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
            vm.section = response.data;
        });

    }
})();
