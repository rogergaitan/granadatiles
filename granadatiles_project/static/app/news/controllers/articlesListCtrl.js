(function () {
    'use strict';

    angular
        .module('app.news')
        .controller('articlesListCtrl',['articleSvc','sectionSvc',
                    articlesListCtrl]);

    function articlesListCtrl(articleSvc) {
        var vm = this;


        vm.saludo = 'hello';

        vm.articles = articleSvc.getArticles();

        vm.title = 'Tile Editorials in Magazines';

        vm.description = 'Magazines love Granada Tile. Click the covers to ﬁnd out what magazine editors are saying about\ ' +
                         'our latest tile news. See our tiles in magazines’ new product roundups and in articles featuring\ ' +
                         'our tiles in residential and commercial projects.';

    }

}());