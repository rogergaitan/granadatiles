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
                catalogListCtrl]);

    function catalogListCtrl(baseSettings,pageSettings, catalogSvc, sectionSvc, sharePageSvc) {

        var vm = this;

        catalogSvc.getCatalogs().then(function (response) {
            vm.catalogs = response.data;
        });

        if(pageSettings.sectionId != 0){
            sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
                vm.section = response.data;
            });
        }

        vm.share = function () {
            sharePageSvc.shareModal();
        };

        vm.menuNewsTemplateUrl = baseSettings.staticUrl + 'app/news/templates/menuNews.html';

        vm.navigation = pageSettings.navigation;

        vm.labels = pageSettings.labels;

        vm.breadcrumds = 'News / Press';
    }

}());