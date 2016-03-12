﻿(function () {
    'use strict';

    angular
        .module('app.portfolio')
        .controller('portfolioHomeCtrl', portfolioHomeCtrl);

    portfolioHomeCtrl.$inject = ['pageSettings', 'sectionSvc', 'baseSettings', 'portfolioSvc'];

    function portfolioHomeCtrl(pageSettings, sectionSvc, baseSettings, portfolioSvc) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.logoutUrl = pageSettings.logoutUrl;
        vm.loggedUser = pageSettings.loggedUser;

        vm.portfolioAsideMenuTemplateURl = baseSettings.staticUrl + 'app/portfolio/templates/portfolioAsideMenu.html'
        
        sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
            vm.section = response.data;
        });

        portfolioSvc.getPortfolioTiles().then(function (response) {
            vm.tiles = response.data;
        });

    }
})();
