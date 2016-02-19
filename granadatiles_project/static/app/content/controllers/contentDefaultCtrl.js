(function () {
    'use strict';

    angular
        .module('app.content')
        .controller('contentDefaultCtrl',
            ['baseSettings',
             'pageSettings',
             'sectionSvc',
             'flatPagesSvc',
             'collectionsSvc',
             'areaSvc',
             contentDefaultCtrl]);


    function contentDefaultCtrl(baseSettings, pageSettings, sectionSvc, flatPagesSvc, collectionsSvc, areaSvc) {
        var vm = this;

        vm.navigation = pageSettings.navigation;
        vm.labels = pageSettings.labels;
        

        vm.productInformationMenuTemplateUrl = baseSettings.staticUrl + 'app/content/templates/productInformationMenu.html';
        vm.menuNewsTemplateUrl = baseSettings.staticUrl + 'app/news/templates/menuNews.html';

        if (pageSettings.sectionId != 0) {
            sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
                vm.section = response.data;
                vm.section.menu = 1;
                setBreadCrumps(1);
                collectionsSvc.getMenuCollections().then(function (response) {
                    vm.menuCollections = response.data;
                });
            });
        }
        else {
            flatPagesSvc.getFlatPage(pageSettings.flatPageTitle).then(function (response) {
                vm.section = response.data;
                if (vm.section.menu == 1) {
                    collectionsSvc.getMenuCollections().then(function (response) {
                        vm.menuCollections = response.data;
                    });
                }
                setBreadCrumps(vm.section.menu);
                flatPagesSvc.getFlatPagesMenu(vm.section.menu).then(function (response) {
                    vm.flatPages = response.data;
                });

            });
        }

        if (pageSettings.areaId != 0) {
            areaSvc.getArea(pageSettings.areaId).then(function (response) {
                vm.area = response.data.description;
            });
        }

        function setBreadCrumps(menuId)
        {
            if (menuId == 1) {
                vm.breadcrumb = {
                    main: pageSettings.labels.productInformation,
                    subMain: vm.section.title
                };
            }
            if (menuId == 2) {
                vm.breadcrumb = {
                    main: pageSettings.labels.newsPress,
                    subMain: vm.section.title
                }
            }
            if (menuId == 3) {
                vm.breadcrumb = {
                    main: pageSettings.labels.aboutUs,
                    subMain: vm.section.title
                }
            }
        }
        
    }
})();
