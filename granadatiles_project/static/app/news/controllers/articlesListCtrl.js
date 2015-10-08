﻿(function () {
    'use strict';

    angular
        .module('app.news')
        .controller('articlesListCtrl',['pageSettings','articleSvc','sectionSvc', articlesListCtrl]);

    function articlesListCtrl(pageSettings, articleSvc) {
        var vm = this;

        vm.breadcrumds = 'My Portafolio';

        vm.title = 'Tile Editorials in Magazines';

        vm.description = '<p>Magazines love Granada Tile. Click the covers to ﬁnd out what magazine editors are saying about\ ' +
                         'our latest tile news. See our tiles in magazines’ new product roundups and in articles featuring\ ' +
                         'our tiles in residential and commercial projects.</p>';

        vm.labels = pageSettings.labels;
         vm.section = pageSettings.sectionId;

        articleSvc.getArticles().then(function (response){
            vm.articles = response.data;
        });

    }

}());