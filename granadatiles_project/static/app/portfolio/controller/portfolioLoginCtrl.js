(function () {
    'use strict';

    angular
        .module('app.portfolio')
        .controller('portfolioLoginCtrl', portfolioLoginCtrl);

    portfolioLoginCtrl.$inject = ['pageSettings',
                                  'appSettings',
                                  '$sce',
                                  'authenticationSvc',
                                  'gtUtilsSvc',
                                  'toastr'];

    function portfolioLoginCtrl(pageSettings, appSettings, $sce, authenticationSvc, gtUtilsSvc, toastr) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.facebookLoginUrls = pageSettings.facebookLoginUrls;
        vm.portfolioLoginsUrls = pageSettings.portfolioLoginsUrls;
        vm.token = $sce.trustAsHtml(pageSettings.token);
        vm.loginResult = pageSettings.loginResult;

       


        vm.activeTemplateUrl = appSettings.staticUrl + 'app/portfolio/templates/login/login.html';

        vm.goToForgotPassword = function () {
            vm.containerCssExtraClass = '';
            vm.activeTemplateUrl = appSettings.staticUrl + 'app/portfolio/templates/login/forgotPassword.html';
        }

        vm.goToLogIn = function () {
            vm.containerCssExtraClass = '';
            vm.activeTemplateUrl = appSettings.staticUrl + 'app/portfolio/templates/login/login.html';
        }

        vm.goToSignUp = function () {
            vm.containerCssExtraClass = 'slide-animate-container-lg';
            vm.activeTemplateUrl = appSettings.staticUrl + 'app/portfolio/templates/login/signUp.html';
        }

        var initialSignup = gtUtilsSvc.getQueryStringParameterByName('signUp')
        if (initialSignup)
            vm.goToSignUp();

        /*Sign up*/

        vm.types = [
           {
               id: 1,
               name: 'Individual'
           }
        ]

        vm.signUp = {
            type: vm.types[0]
        }

        vm.signUpUser = function () {
            vm.signUp.recaptchaResponse = vm.response;
            authenticationSvc.registerUser(vm.signUp)
                .then(function (response) {
                    window.location = response.redirect_url;
                }, function (error) {
                    toastr.error("Something went wrong with your signup, please try again later", "Error")
                });
        }


        /*recaptcha*/

        vm.key = '6LdcMRcTAAAAALCmZ-3TdMsExELDsQvytBlq0qSl';
        vm.response = null;

        vm.setWidgetId = function (widgetId) {
            vm.widgetId = widgetId;
        }

        vm.cbExpiration = function () {
            vm.response = null;
            vm.recaptchaCompleted = false;
        }

        vm.setResponse = function (response) {
            vm.recaptchaCompleted = true;
            vm.response = response;
        }

    }
})();
