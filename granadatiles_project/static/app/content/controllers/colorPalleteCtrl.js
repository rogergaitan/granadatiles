(function () {
    'use strict';

    angular
        .module('app.content')
        .controller('colorPalleteCtrl', colorPalleteCtrl);

    colorPalleteCtrl.$inject = ['baseSettings', 'pageSettings', 'tilesSvc', 'sectionSvc', 'collectionsSvc', 'flatPagesSvc'];

    function colorPalleteCtrl(baseSettings, pageSettings, tilesSvc, sectionSvc, collectionsSvc, flatPagesSvc) {
        /* jshint validthis:true */
        var vm = this;
        vm.navigation = baseSettings.navigation;
        vm.labels = pageSettings.labels;
      

        vm.productInformationMenuTemplateUrl = baseSettings.staticUrl + 'app/content/templates/productInformationMenu.html';

        sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
            vm.section = response.data;
            vm.breadcrumb = {
                main: pageSettings.labels.productInformation,
                subMain: vm.section.title
            };
        });

        collectionsSvc.getMenuCollections().then(function (response) {
            vm.menuCollections = response.data;
        });

        tilesSvc.getColorPallete().then(function (response) {
            vm.colors = response.data;
        });

        flatPagesSvc.getFlatPagesMenu(1).then(function (response) {
            vm.flatPages = response.data;
        });
    }
})();
