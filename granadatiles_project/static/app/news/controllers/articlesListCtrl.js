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

        /*articleSvc.getArticles().then(function (response){
            vm.articles = response.data;
        });*/

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

        vm.menuNewsTemplateUrl = baseSettings.staticUrl + 'app/news/templates/menuNews.html';

        vm.navigation = pageSettings.navigation;

        vm.labels = pageSettings.labels;

        vm.breadcrumds = 'My Portafolio';

        vm.status = {
            isopen: false
        };

        vm.setYear = function(year) {
            vm.selectedYear = year;
            updateArticles(year.year);
        };

        function updateArticles(selectedYear){
            console.log(selectedYear);
            articleSvc.getArticlesFiltered(selectedYear).then(function (response){
                vm.articles = response.data;
                console.log(vm.articles[0].id);
            });
        }


    }

}());