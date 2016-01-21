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
        console.log(vm.labels);

        var selectedTileId = $scope.shared.tileId;

        /*TODO: Llamar el metodo del servicio para obtener los datos del tile aqui
           y enlazar los datos */


        vm.backToGroup = function () {
            $scope.shared.tileDetailTemplateUrl = '';
        }
    }
})();
