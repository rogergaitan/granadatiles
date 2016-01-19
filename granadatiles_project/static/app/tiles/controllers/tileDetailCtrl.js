(function () {
    'use strict';

    angular
        .module('app')
        .controller('tileDetailCtrl', tileDetailCtrl);

    tileDetailCtrl.$inject = ['$location', '$scope', 'tilesSvc'];

    function tileDetailCtrl($location, $scope, tilesSvc) {
        var vm = this;
        vm.title = 'tileDetail';

        var selectedTileId = $scope.shared.tileId;

        /*TODO: Llamar el metodo del servicio para obtener los datos del tile aqui
           y enlazar los datos */


        vm.backToGroup = function () {
            $scope.shared.tileDetailTemplateUrl = '';
        }
    }
})();
