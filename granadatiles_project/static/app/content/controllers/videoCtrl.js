(function () {
    'use strict';

    angular
        .module('app.content')
        .controller('videoCtrl',
            ['baseSettings',
                'pageSettings',
                'videoSvc',
                'sectionSvc',
                'flatPagesSvc',
                videoCtrl]);

    function videoCtrl(baseSettings, pageSettings, videoSvc, sectionSvc, flatPagesSvc) {
        var vm = this;

        videoSvc.getVideos().then(function (response) {
            vm.videos = response.data;
        });

        flatPagesSvc.getFlatPagesMenu(2).then(function (response) {
            vm.flatPages = response.data;
        });

         if(pageSettings.sectionId != 0){
             sectionSvc.getSection(pageSettings.sectionId).then(function(response){
                vm.section = response.data;
            });
         }

        vm.menuNewsTemplateUrl = baseSettings.staticUrl + 'app/news/templates/menuNews.html';

        vm.navigation = pageSettings.navigation;

        vm.labels = pageSettings.labels;

    }

}());