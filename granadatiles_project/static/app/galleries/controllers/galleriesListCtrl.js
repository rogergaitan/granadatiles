(function () {
    'use strict';

    angular
        .module('app.galleries')
        .controller('galleryListCtrl',['gallerySvc','sectionSvc',
                    galleryCtrl]);

    function galleryCtrl(gallerySvc, sectionSvc) {
        var vm = this;

        vm.galleries = gallerySvc.getGalleries();
        vm.section = gallerySvc.getSection();

    }

}());