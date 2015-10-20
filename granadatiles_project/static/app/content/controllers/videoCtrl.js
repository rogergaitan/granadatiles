(function () {
    'use strict';

    angular
        .module('app.content')
        .controller('videoCtrl',
            ['baseSettings',
                'pageSettings',
                'videoSvc',
                'sectionSvc',
                videoCtrl]);

    function videoCtrl(baseSettings, pageSettings, videoSvc, sectionSvc) {
        var vm = this;

        videoSvc.getVideos().then(function (response) {
            vm.videos = response.data;
        });

         if(pageSettings.sectionId != 0){
             sectionSvc.getSection(pageSettings.sectionId).then(function(response){
                vm.section = response.data;
            });
         }

        vm.menuNewsTemplateUrl = baseSettings.staticUrl + 'app/news/templates/menuNews.html';

        vm.navigation = pageSettings.navigation;

        vm.labels = pageSettings.labels;

        vm.breadcrumds = 'News / Press';
    }

}());