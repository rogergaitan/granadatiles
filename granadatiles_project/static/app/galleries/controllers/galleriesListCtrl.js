(function () {
    'use strict';

    angular
        .module('app.galleries')
        .controller('galleryListCtrl',['gallerySvc','sectionSvc',
                    galleryCtrl]);

    function galleryCtrl(gallerySvc) {
        var vm = this;

        vm.otro = "hola";

        gallerySvc.getGalleries().then(function (response){
            vm.galleries = response.data;
        })



    }

}());