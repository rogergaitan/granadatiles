(function () {
    'use strict';

    angular
        .module('app')
        .controller('tileDetailCtrl', tileDetailCtrl);

    tileDetailCtrl.$inject = ['$location', '$scope', 'tilesSvc','pageSettings'];

    function tileDetailCtrl($location, $scope, tilesSvc, pageSettings) {
        var vm = this;
        vm.title = 'tileDetail';

        vm.labels = pageSettings.labels;

        var selectedTileId = $scope.shared.tileId;
        

        vm.backToGroup = function () {
            $scope.shared.tileDetailTemplateUrl = '';
        };

        tilesSvc.getTileDetail(selectedTileId).then(function (response){
            vm.tile = response.data;
            if(vm.tile.sizes.length > 0){
                vm.selectedSize = vm.tile.sizes[0].size
            }
        });

        vm.setSize = function (size) {
            vm.selectedSize = size.size;
        };
    }
})();
