(function () {
    'use strict';

    angular
        .module('app')
        .controller('customTilesCtrl', customTileCtrl);

    customTileCtrl.$inject = ['pageSettings', 'customTilesSvc', 'initData', '$modalInstance'];

    function customTileCtrl(pageSettings, customTilesSvc, initData, $modalInstance) {
        /* jshint validthis:true */
        var vm = this;

        vm.labels = pageSettings.labels;
        vm.navigation = pageSettings.navigation;
        vm.colorsUsed = [];

        vm.colorPallete = initData.colorPallete;
        vm.tile = initData.tileData;
        vm.colorsUsed = vm.tile.colors;
        customTilesSvc.getTilePlane(vm.tile.plane).then(function (response) {
            vm.plane = response.data;
        });

        console.log(vm.tile);

        vm.close = function () {
            $modalInstance.dismiss('cancel');
        };
    }
})();
