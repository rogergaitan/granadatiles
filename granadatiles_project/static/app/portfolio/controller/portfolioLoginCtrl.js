(function () {
    'use strict';

    angular
        .module('app.portfolio')
        .controller('portfolioLoginCtrl', portfolioLoginCtrl);

    portfolioLoginCtrl.$inject = ['pageSettings', 'appSettings'];

    function portfolioLoginCtrl(pageSettings, appSettings) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.facebookLoginUrls = pageSettings.facebookLoginUrls;

        vm.activeTemplateUrl = appSettings.staticUrl + 'app/portfolio/templates/login/login.html';

        vm.goToForgotPassword = function () {
            vm.activeTemplateUrl = appSettings.staticUrl + 'app/portfolio/templates/login/forgotPassword.html';
        }

        vm.goToLogIn = function () {
            vm.activeTemplateUrl = appSettings.staticUrl + 'app/portfolio/templates/login/login.html';
        }

        vm.goToSignUp = function () {
            vm.activeTemplateUrl = appSettings.staticUrl + 'app/portfolio/templates/login/signUp.html';
        }
    }
})();
