(function () {
    'use strict';

    angular
        .module('app')
        .controller('contentDefaultCtrl',
            ['baseSettings',
             'pageSettings',
             'sectionSvc',
             'collectionsSvc',
             contentDefaultCtrl]);


    function contentDefaultCtrl(baseSettings, pageSettings, sectionSvc, collectionsSvc) {
        var vm = this;
        
        vm.productInformationMenuTemplateUrl = baseSettings.staticUrl + 'app/content/templates/productInformationMenu.html';
        
        sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
            vm.section = response.data;
        });
        
        collectionsSvc.getMenuCollections().then(function (response) {
            vm.menuCollections = response.data;
        })


        vm.breadcrumb = pageSettings.labels.collections;
    }
})();
