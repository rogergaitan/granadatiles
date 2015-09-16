(function () {
    'use strict';

    angular
        .module('app.core', [])
        .constant('appSettings', {
            serverPath: '/api/',
            staticUrl: '/static/',
            areas: {
                SLOGAN: 1, // Page 1  Cement tile is not just a tile...
                WELCOME: 2, // Page 1 Get inspired by Residential and Commercial...
            }
        });
}());