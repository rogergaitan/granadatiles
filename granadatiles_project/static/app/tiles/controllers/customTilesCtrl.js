﻿(function () {
    'use strict';

    angular
        .module('app')
        .controller('customTilesCtrl', customTileCtrl);

    customTileCtrl.$inject = ['pageSettings', 'customTilesSvc', 'initData', '$modalInstance', '$timeout', 'cartSvc', 'toastr'];

    function customTileCtrl(pageSettings, customTilesSvc, initData, $modalInstance, $timeout, cartSvc, toastr) {
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
        vm.notAuthenticated = false;

        if (pageSettings.loggedUser == "AnonymousUser")
            vm.notAuthenticated = true;

        customTilesSvc.getTilePlane(vm.tile.plane).then(function (response) {
            vm.plane = response.data;
            vm.mosaic = response.data;
            $timeout(function () {
                for (var i = 0; i < vm.tile.colorGroups.length; i++) {
                    var $parentContainer = $('#painting-container');
                    var groupName = customTilesSvc.formatGroupName(vm.tile.colorGroups[i].group);
                    var $group = $parentContainer.find('#' + groupName);
                    customTilesSvc.paintColor($group, vm.tile.colorGroups[i].color.hexadecimalCode);
                    vm.mosaic = $parentContainer.html();
                    vm.planeLoaded = true;
                }
                if(vm.tile.isNotSquare)
                    $('.not-square-row').css('height', parseFloat($('.tile-not-square-plane svg').css('height')) - 0.025);
                if (vm.notAuthenticated) {
                    toastr.warning(vm.labels.notAuthenticatedCustom, 'Warning')
                }
            }, 400);
        });


        vm.close = function () {
            $modalInstance.dismiss('cancel');
        };

        vm.addColor = function (event, data) {
            var targetElement = event.originalEvent.target;
            vm.dropedColor = data;
            var group;

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

            var colorGroup = vm.colorGroups.find(function (colorGroup) {
                return (colorGroup.group == group)
            });

            if (colorGroup) {
                colorGroup.colorId = vm.dropedColor.id;
                colorGroup.colorName = vm.dropedColor.name;
                if(colorGroup.colorHexadecimalCode != vm.dropedColor.hexadecimalCode)
                    vm.hasChanges = true;
                colorGroup.colorHexadecimalCode = vm.dropedColor.hexadecimalCode;
            }
            else {
                vm.colorGroups.push({
                    colorId: vm.dropedColor.id,
                    group: group,
                    colorName: vm.dropedColor.name,
                    colorHexadecimalCode: vm.dropedColor.hexadecimalCode
                });
                vm.hasChanges = true;
            }
            vm.colorsUsed = [];
            vm.colorGroups.forEach(function (colorGroup) {
                var color = vm.colorsUsed.find(function (color) { return color.id == colorGroup.colorId });
                if (!color) {
                    vm.colorsUsed.push({
                        hexadecimalCode: colorGroup.colorHexadecimalCode,
                        id: colorGroup.colorId,
                        name: colorGroup.colorName
                    });
                }
            });
        }

        vm.saveToPortfolio = function () {
            var sendObject = {
                tileId: vm.tile.id,
                colorGroups: vm.colorGroups
            }
            if (vm.tile.customizedTileId) {
                customTilesSvc.addColorGroup(vm.tile.customizedTileId, sendObject).then(function (response) {
                    vm.hasChanges = false;
                    toastr.success(vm.labels.changesSave, vm.labels.success);
                }, function (error) {
                    var messages = error.data
                    displayErrors(messages);
                });
            }
            else {
                customTilesSvc.addCustomizedTile(sendObject).then(function (response) {
                    vm.tile.customizedTileId = response.data.customizedTileId;
                    vm.hasChanges = false;
                    toastr.success(vm.labels.tileAdded, vm.labels.success);
                }, function (error) {
                    var messages = error.data
                    displayErrors(messages);
                });
            }
        }

        vm.addToCart = function () {
            var sendObject = {
                customizedTileId: vm.tile.customizedTileId,
            }
            cartSvc.addCustomizedTile(sendObject).then(function (response) {
                var cart = cartSvc.getCart();
                cartSvc.setCartCount(cart.count + 1);
                toastr.success(vm.labels.tileAddedCart, vm.labels.success);
            }, function (error) {
                var messages = error.data
                displayErrors(messages);
            });
        }

        vm.orderSample = function () {

        }

        function displayErrors(messages) {
            if (messages.constructor == Array) {
                messages.forEach(function (message) {
                    toastr.warning(message, 'Warning');
                });
            } else {
                for (var key in messages) {
                    toastr.warning(messages[key], 'Warning');
                }
            }
        }

    }
})();
