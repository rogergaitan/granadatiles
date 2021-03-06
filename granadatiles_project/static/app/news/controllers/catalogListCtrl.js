(function () {
    'use strict';

    angular
        .module('app.news')

        .controller('catalogListCtrl',
            ['baseSettings',
                'pageSettings',
                'catalogSvc',
                'sectionSvc',
                'sharePageSvc',
                'flatPagesSvc',
                catalogListCtrl]);

    function catalogListCtrl(baseSettings, pageSettings, catalogSvc, sectionSvc, sharePageSvc, flatPagesSvc) {

        var vm = this;

        catalogSvc.getCatalogs().then(function (response) {
            vm.catalogs = response.data;
        });

        flatPagesSvc.getFlatPagesMenu(2).then(function (response) {
            vm.flatPages = response.data;
        });

        if(pageSettings.sectionId != 0){
            sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
                vm.section = response.data;
            });
        }

        vm.share = function () {
            sharePageSvc.shareModal(window.location.href);
        };

        vm.menuNewsTemplateUrl = baseSettings.staticUrl + 'app/news/templates/menuNews.html';

        vm.navigation = pageSettings.navigation;

        vm.labels = pageSettings.labels;

    }

}());