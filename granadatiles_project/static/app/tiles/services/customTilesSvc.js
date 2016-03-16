(function () {
    'use strict';

    angular
        .module('app')
        .factory('customTilesSvc', customTilesSvc);

    customTilesSvc.$inject = ['baseSettings', 'tilesSvc', '$http', '$modal'];

    function customTilesSvc(baseSettings, tilesSvc, $http, $modal) {
        var service = {
            customTileModal: customTileModal,
            getTilePlane: getTilePlane
        };

        return service;

        function getTilePlane(url) {
            return $http.get(window.location.origin + url);
        }

        function customTileModal(tileData) {
            $modal.open({
                templateUrl: baseSettings.staticUrl + 'app/tiles/templates/customTile.html',
                controller: 'customTilesCtrl',
                controllerAs: 'vm',
                size: 'lg',
                windowClass: 'modal-custom-tile',
                resolve: {
                    initData: function () {
                        return tilesSvc.getColorPallete().then(function (response) {
                            return {
                                tileData: tileData,
                                colorPallete: response.data
                            };
                        });
                    }
                }
            });
        }
    }
})();