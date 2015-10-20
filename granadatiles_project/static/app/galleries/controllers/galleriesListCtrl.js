(function () {
    'use strict';

    angular
        .module('app.galleries')
        .controller('galleryListCtrl',
                    ['baseSettings',
                    'pageSettings',
                    'gallerySvc',
                    'sectionSvc',
                    '$modal',
                    galleryCtrl]);

    function galleryCtrl(baseSettings, pageSettings, gallerySvc, sectionSvc, $modal) {
        var vm = this;

        gallerySvc.getGalleries().then(function (response) {
            vm.galleries = response.data;
        });

        if(pageSettings.sectionId != 0){
            sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
                vm.section = response.data;
            });
        }

        vm.showGallery = function (categoryId) {
            $modal.open({
                templateUrl: baseSettings.staticUrl + 'app/galleries/templates/galleryModal.html',
                controller: 'galleryModalCtrl',
                controllerAs: 'vm',
                size:'lg',
                resolve:{
                    gallery: function () {
                        return gallerySvc.getGallery(categoryId).then(function (response) {
                            return response.data;
                        });
                    }
                }
            })
        };

        vm.breadcrumds = 'Gallery';
    }

}());