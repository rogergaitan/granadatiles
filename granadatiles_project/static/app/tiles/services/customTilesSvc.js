(function () {
    'use strict';

    angular
        .module('app')
        .factory('customTilesSvc', customTilesSvc);

    customTilesSvc.$inject = ['appSettings', 'baseSettings', 'tilesSvc', '$http', '$modal'];

    function customTilesSvc(appSettings, baseSettings, tilesSvc, $http, $modal) {
        var service = {
            customTileModal: customTileModal,
            getTilePlane: getTilePlane,
            addCustomizedTile: addCustomizedTile,
            addColorGroup: addColorGroup
        };

        return service;

        function getTilePlane(url) {
            return $http.get(window.location.origin + url);
        }

        function addCustomizedTile(customizedTile) {
            return $http.post(appSettings.serverPath + 'customizedtiles/', customizedTile);
        }

        function addColorGroup(customizedTileId, customizedTile) {
            return $http.post(appSettings.serverPath + 'customizedtiles/' + customizedTileId + '/groupcolors/', customizedTile)
        }

        function customTileModal(tileData) {
            return $modal.open({
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