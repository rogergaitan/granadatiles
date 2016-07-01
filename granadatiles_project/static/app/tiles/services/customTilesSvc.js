(function () {
    'use strict';

    angular
        .module('app')
        .factory('customTilesSvc', customTilesSvc);

    customTilesSvc.$inject = ['appSettings', 'baseSettings', 'tilesSvc', '$http', '$modal', '$timeout'];

    function customTilesSvc(appSettings, baseSettings, tilesSvc, $http, $modal, $timeout) {
        var service = {
            customTileModal: customTileModal,
            getTilePlane: getTilePlane,
            addCustomizedTile: addCustomizedTile,
            addColorGroup: addColorGroup,
            formatColorGroupsForPost: formatColorGroupsForPost,
            getColorsUsed: getColorsUsed,
            formatGroupName: formatGroupName
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

        function formatColorGroupsForPost(colorGroups) {
            var formatedColorGroups = [];
            colorGroups = colorGroups || [];
            for (var i = 0; i < colorGroups.length; i++) {
                formatedColorGroups.push({
                    colorId: colorGroups[i].color.id,
                    group: colorGroups[i].group,
                    colorHexadecimalCode: colorGroups[i].color.hexadecimalCode,
                    colorName: colorGroups[i].color.name
                });
            }
            return formatedColorGroups;
        }

        function getColorsUsed(colorGroups) {
            var colorsUsed = [];
            colorGroups = colorGroups || [];
            for (var i = 0; i < colorGroups.length; i++) {
                var index = colorsUsed.map(function (color) { return color.id; }).indexOf(colorGroups[i].color.id);
                if (index != -1)
                    continue;
                colorsUsed.push({
                    name: colorGroups[i].color.name,
                    id: colorGroups[i].color.id,
                    hexadecimalCode: colorGroups[i].color.hexadecimalCode,
                });
            }
            return colorsUsed;
        }

        function customTileModal(tileData) {
            var instance = $modal.open({
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
            instance.rendered.then(function () {
                $timeout(function () {
                    $('.initial-hide').show();
                }, 500);
            })
            return instance;
        }

        function formatGroupName(groupName) {
            if (!groupName.startsWith("G")) {
                groupName = "G" + groupName;
            }
            
            return groupName;
        }
    }
})();