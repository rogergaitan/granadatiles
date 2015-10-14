(function () {
    'use strict';

    angular
        .module('app.core', [])
        .constant('appSettings', {
            serverPath: '/api/',
            staticUrl: '/static/',
            areas: {
                SLOGAN: 1, // Page 1  Cement tile is not just a tile...
                COMPAREPRODUCTS: 2, //Page 18 Comparision table...
                CEMENTVSCERAMIC: 3, // Page 19 Cement vs ceramic...
            }
        });
}());