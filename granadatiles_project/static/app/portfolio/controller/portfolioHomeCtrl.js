﻿(function () {
    'use strict';

    angular
        .module('app.portfolio')
        .controller('portfolioHomeCtrl', portfolioHomeCtrl);

    portfolioHomeCtrl.$inject = ['pageSettings', 'sectionSvc', 'baseSettings', 'portfolioSvc', 'sharePageSvc', 'authenticationSvc'];

    function portfolioHomeCtrl(pageSettings, sectionSvc, baseSettings, portfolioSvc, sharePageSvc, authenticationSvc) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.navigation = pageSettings.navigation;
        vm.logoutUrl = pageSettings.logoutUrl;
        vm.loggedUser = pageSettings.loggedUser;

        vm.portfolioAsideMenuTemplateURl = baseSettings.staticUrl + 'app/portfolio/templates/portfolioAsideMenu.html'
        
        sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
            vm.section = response.data;
        });

        portfolioSvc.getPortfolioTiles().then(function (response) {
            vm.tiles = response.data;
        });

        vm.removeTile = function (tile) {
            portfolioSvc.removeTile(tile.portfoliotile_id).then(function (response) {
                tile.removed = true;
            });
        }
        vm.shareTile = function (tile) {
            sharePageSvc.shareModal(tile.url);
        };

        vm.myAccount = function () {
            authenticationSvc.myAccountModal(vm.loggedUser)
        };
    }
})();
