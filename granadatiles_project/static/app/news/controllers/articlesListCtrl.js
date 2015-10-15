(function () {
    'use strict';

    angular
        .module('app.news')
        .controller('articlesListCtrl',
            ['pageSettings',
                'baseSettings',
                'articleSvc',
                'sectionSvc',
                articlesListCtrl]);

    function articlesListCtrl(pageSettings, baseSettings, articleSvc, sectionSvc) {
        var vm = this;

        articleSvc.getArticles().then(function (response){
            vm.articles = response.data;
        });

        articleSvc.getYears().then(function (response){
            vm.years = response.data;
        });

        articleSvc.getArticlesFiltered().then(function (response){
            vm.articlesFiltered = response.data;
        });

        if(pageSettings.sectionId != 0){
            sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
                vm.section = response.data;
            });
        }

        vm.menuNewsTemplateUrl = baseSettings.staticUrl + 'app/news/templates/menuNews.html';

        vm.navigation = pageSettings.navigation;

        vm.labels = pageSettings.labels;

        vm.breadcrumds = 'My Portafolio';

    }

}());