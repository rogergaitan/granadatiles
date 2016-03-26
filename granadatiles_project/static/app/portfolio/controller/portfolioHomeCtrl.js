(function () {
    'use strict';

    angular
        .module('app.portfolio')
        .controller('portfolioHomeCtrl', portfolioHomeCtrl);

    portfolioHomeCtrl.$inject = ['pageSettings', 'sectionSvc', 'baseSettings', 'portfolioSvc', 'sharePageSvc', 'authenticationSvc', 'customTilesSvc', 'tilesSvc', 'gtDialogsSvc', 'cartSvc'];

    function portfolioHomeCtrl(pageSettings, sectionSvc, baseSettings, portfolioSvc, sharePageSvc, authenticationSvc, customTilesSvc, tilesSvc, gtDialogsSvc, cartSvc) {
        /* jshint validthis:true */
        var vm = this;
        vm.labels = pageSettings.labels;
        vm.navigation = pageSettings.navigation;
        vm.logoutUrl = pageSettings.logoutUrl;
        vm.loggedUser = pageSettings.loggedUser;

        vm.portfolioAsideMenuTemplateURl = baseSettings.staticUrl + 'app/portfolio/templates/portfolioAsideMenu.html'

        sectionSvc.getSection(pageSettings.sectionId).then(function (response) {
            vm.section = response.data;
        });

        portfolioSvc.getPortfolioTiles().then(function (response) {
            vm.tiles = response.data;
        });

        vm.buyTile = function (tile) {
            if (tile.isCustomTile) {
                var sendObject = {
                    customizedTileId: tile.portfoliotile_id,
                }
                cartSvc.addCustomizedTile(sendObject).then(function (response) {
                    var cart = cartSvc.getCart();
                    cartSvc.setCartCount(cart.count + 1);
                });
            }
            else {
                var cartItem = {
                    id: tile.id
                };
                cartSvc.addTile(cartItem).then(function (resp) {
                    var cart = cartSvc.getCart();
                    cartSvc.setCartCount(cart.count + 1);
                });
            }
        };

        vm.removeTile = function (tile) {
            var instance = gtDialogsSvc.confirmModal(vm.labels.removeTile);
            instance.result.then(function () {
                portfolioSvc.removeTile(tile.portfoliotile_id, tile.isCustomTile).then(function (response) {
                    tile.removed = true;
                });
            })
        }
        vm.shareTile = function (tile) {
            sharePageSvc.shareModal(tile.url);
        };

        vm.myAccount = function () {
            authenticationSvc.myAccountModal(vm.loggedUser)
        };

        vm.editTile = function (tile) {
            tilesSvc.getTileDetail(tile.id).then(function (response) {
                var tileData = response.data;
                tileData.colorGroups = tile.colorGroups;
                if (tile.isCustomTile)
                    tileData.customizedTileId = tile.portfoliotile_id;

                var modalInstance = customTilesSvc.customTileModal(tileData);

                modalInstance.result.then(function () {
                }, function () {
                    vm.tiles = [];
                    portfolioSvc.getPortfolioTiles().then(function (response) {
                        vm.tiles = response.data;
                    });
                });
            });
        }
    }
})();
