(function () {
    'use strict';

    angular
        .module('app')
        .controller('flatPagesMenuCtrl', flatPagesMenuCtrl);

    flatPagesMenuCtrl.$inject = ['baseSettings', 'flatPagesSvc'];

    function flatPagesMenuCtrl(baseSettings, flatPagesSvc) {
        /* jshint validthis:true */
        var vm = this;

        vm.newsPressFlatPagesMenuUrl = baseSettings.staticUrl + 'app/content/templates/newsPressFlatPagesMenu.html';
        vm.aboutUsFlatPagesMenuUrl = baseSettings.staticUrl + 'app/content/templates/aboutUsFlatPagesMenu.html';

        flatPagesSvc.getFlatPagesMenu(2).then(function (response) {
            vm.newsPressFlatPages = response.data;
        });

        flatPagesSvc.getFlatPagesMenu(3).then(function (response) {
            vm.aboutUsFlatPages = response.data;
        });

    }
})();
