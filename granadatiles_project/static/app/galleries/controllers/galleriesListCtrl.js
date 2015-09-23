(function () {
    'use strict';

    angular
        .module('app.galleries')
        .controller('galleryListCtrl',['gallerySvc','sectionSvc',
                    galleryCtrl]);

    function galleryCtrl(gallerySvc) {
        var vm = this;

        vm.galleries = gallerySvc.getGalleries();

        vm.title = 'Photos of Cement & Concrete Tile Installations';

        vm.description = 'Granada Tile is pleased to share photos of some of the cement tile installations using our ﬂagship\ ' +
            'Echo Collection tiles. Our hand made cement and concrete tiles have been used in private residences and commercial\ ' +
            'projects, indoors and outdoors, and on ﬂoors and on walls (and even on ceilings). These cement and concrete tile\ ' +
            'installation photos feature bathroom tile, kitchen tile, tile backslashes, wall tiles, ﬂoor tiles, commercial tiles,\ ' +
            'restaurant tiles, spa tiles, and patio tiles.' + '<br>'+ 'Depending on the setting, some of these hand made cement tiles\ ' +
            'evoke French and Moroccan tiles, such as the Bouchon Bistro in Beverly Hills and the Fez entryway to a Moroccan-style\ ' +
            'private residence. Other tile installations attain a chic modern esthetic, like the Delphine Restaurant in the W. Hotel\ ' +
            'and the Serengeti tile at the Terranea Resort and Spa.' + '<br>' + 'Where will you install your Echo Collection cement and\ ' +
            'concrete tiles? (And when you do, please send pictures so we can add them here!)';


        /*gallerySvc.getGalleries().then(function (response){
            vm.galleries = response.data;
        })*/





    }

}());