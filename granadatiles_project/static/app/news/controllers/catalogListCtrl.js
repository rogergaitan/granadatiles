(function () {
    'use strict';

    angular
        .module('app.news')
        .controller('catalogListCtrl',['catalogSvc','sectionSvc',
                    catalogListCtrl]);

    function catalogListCtrl(catalogSvc) {
        var vm = this;

        catalogSvc.getCatalogs().then(function (response){
            vm.catalogs = response.data;
        })

        vm.breadcrumds = 'News / Press';

        //vm.catalogs = catalogSvc.getCatalogs();

        vm.title = 'Tile Design Inspiration to Help You Design Your Project';

        vm.description = '<p>As we all know, design inspiration can come from many di?erent sources: a friends home, a\ ' +
                        'shop window, a photograph. We o?er you our book of photos of tile installations and tile design.\ ' +
                        'We hope it provides a spark of inspiration for some aspect of your project. Once you complete\ ' +
                        'your project, we hope youll share your photos so others might derive tile design inspiration from\ ' +
                        'them.</p><p>Granada Tile has developed a number of di?erent catalogs of our tile over the years.\ ' +
                        'Because we are constantly adding to our collections, it has proven to be a challenge to keep the\ ' +
                        'cement tile catalogs completely up-to-date. As a result, we have relied more and more on the web\ ' +
                        'site to bring you the most current designs and patterns. (This is also an environmentally friendly\ ' +
                        'solution.)</p><p>Nevertheless, the most recent cement tile catalogs are still useful tools and can\ ' +
                        'present information and photos in ways that inspire and inform.</p>';

    }

}());