(function () {
    'use strict';

    angular
        .module('app.news')
        .controller('articlesListCtrl',
            ['pageSettings',
                'baseSettings',
                'articleSvc',
                'sectionSvc',
                'flatPagesSvc',
                articlesListCtrl]);

    function articlesListCtrl(pageSettings, baseSettings, articleSvc, sectionSvc, flatPagesSvc) {
        var vm = this;

        articleSvc.getYears().then(function (response){
            vm.years = response.data;
            vm.selectedYear = vm.years[0];
            updateArticles(vm.years[0].year);
        });

        if(pageSettings.sectionId != 0){
            sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
                vm.section = response.data;
            });
        }

        flatPagesSvc.getFlatPagesMenu(2).then(function (response) {
            vm.flatPages = response.data;
        });

        vm.menuNewsTemplateUrl = baseSettings.staticUrl + 'app/news/templates/menuNews.html';

        vm.navigation = pageSettings.navigation;

        vm.labels = pageSettings.labels;

        vm.breadcrumds = 'My Portafolio';

        vm.setYear = function(year) {
            vm.selectedYear = year;
            updateArticles(year.year);
        };

        function updateArticles(selectedYear){
            articleSvc.getArticlesFiltered(selectedYear).then(function (response){
                vm.articles = response.data;
            });
        }


    }

}());