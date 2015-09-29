(function () {
    'use strict';

    angular
        .module('app.news')
        .controller('articlesListCtrl',['articleSvc','sectionSvc',
                    articlesListCtrl]);

    function articlesListCtrl(articleSvc) {
        var vm = this;


        vm.breadcums = 'My Portafolio';

        vm.articles = articleSvc.getArticles();

        vm.title = 'Tile Editorials in Magazines';

        vm.description = '<p>Magazines love Granada Tile. Click the covers to ﬁnd out what magazine editors are saying about\ ' +
                         'our latest tile news. See our tiles in magazines’ new product roundups and in articles featuring\ ' +
                         'our tiles in residential and commercial projects.</p>';

        articleSvc.getArticles().then(function (response){
            vm.articles = response.data;
        })

        //console.log(vm.articles().length);

    }

}());