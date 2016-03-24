(function () {
    'use strict';

    angular
        .module('app')
        .controller('customTilesCtrl', customTileCtrl);

    customTileCtrl.$inject = ['pageSettings', 'customTilesSvc', 'initData', '$modalInstance', '$timeout'];

    function customTileCtrl(pageSettings, customTilesSvc, initData, $modalInstance, $timeout) {
        /* jshint validthis:true */
        var vm = this;
        vm.hasChanges = false;
        vm.planeLoaded = false;
        vm.labels = pageSettings.labels;
        vm.navigation = pageSettings.navigation;
        vm.colorsUsed = [];

        vm.colorPallete = initData.colorPallete;
        vm.tile = initData.tileData;
        vm.colorGroups = customTilesSvc.formatColorGroupsForPost(vm.tile.colorGroups);
        vm.colorsUsed = customTilesSvc.getColorsUsed(vm.tile.colorGroups);

        customTilesSvc.getTilePlane(vm.tile.plane).then(function (response) {
            vm.plane = response.data;
            vm.mosaic = response.data;
            $timeout(function () {
                for (var i = 0; i < vm.tile.colorGroups.length; i++) {
                    var $parentContainer = $('#painting-container');
                    $parentContainer.find('#' + vm.tile.colorGroups[i].group).css('fill', vm.tile.colorGroups[i].color.hexadecimalCode);
                    vm.mosaic = $parentContainer.html();
                    vm.planeLoaded = true;
                }
            }, 100);
        });


        vm.close = function () {
            $modalInstance.dismiss('cancel');
        };

        vm.addColor = function (event, data) {
            var targetElement = event.originalEvent.target;
            vm.dropedColor = data;
            var index = vm.colorsUsed.map(function (color) { return color.id; }).indexOf(vm.dropedColor.id);
            var group;
            if (index === -1)
                vm.colorsUsed.push(vm.dropedColor);

            var isGroup = false;
            if (!targetElement.id) {
                targetElement = targetElement.parentNode;
                isGroup = true;
                group = $(targetElement).attr('id');
            }

            if (isGroup) {
                $.each($(targetElement).children(), function (index, path) {
                    $(path).attr('fill', vm.dropedColor.hexadecimalCode);
                    $(path).css('fill', vm.dropedColor.hexadecimalCode);
                })
            }
            else {
                var id = $(targetElement).attr('id');
                group = id;
                $(targetElement).attr('fill', vm.dropedColor.hexadecimalCode);
                $(targetElement).css('fill', vm.dropedColor.hexadecimalCode);
            }

            vm.mosaic = $(event.currentTarget).html();
            var count = vm.colorGroups.filter(function (colorGroup) {
                return (colorGroup.colorId == vm.dropedColor.id && colorGroup.group == group)
            }).length;
            if (count == 0) {
                vm.colorGroups.push({
                    colorId: vm.dropedColor.id,
                    group: group
                });
                vm.hasChanges = true;
            }
        }

        vm.saveToPortfolio = function () {
            var sendObject = {
                tileId: vm.tile.id,
                colorGroups: vm.colorGroups
            }
            if (vm.tile.customizedTileId) {
                customTilesSvc.addColorGroup(vm.tile.customizedTileId, sendObject).then(function (response) {
                    vm.hasChanges = false;
                });
            }
            else {
                customTilesSvc.addCustomizedTile(sendObject).then(function (response) {
                    vm.tile.customizedTileId = response.data.customizedTileId;
                    vm.hasChanges = false;
                });
            }

        }

    }
})();
