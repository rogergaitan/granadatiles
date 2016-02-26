(function () {
    'use strict';

    angular
        .module('app')
        .factory('tilesLogicSvc', tilesLogicSvc);


    function tilesLogicSvc() {
        var service = {
            calculateQuantityInBox: calculateQuantityInBox,
            calculatePricePerBox: calculatePricePerBox
        };

        return service;

        function calculateQuantityInBox(tile) {
            if (tile.box.measurementUnit == 1 && !tile.qtyIsSqFt) {
                return tile.quantity/tile.box.quantity
            }

            if (tile.box.measurementUnit == 2 && tile.qtyIsSqFt) {
                return tile.quantity/tile.box.quantity
            }

            if (tile.box.measurementUnit == 1 && tile.qtyIsSqFt) {
                return (tile.quantity * tile.sqFt) / tile.box.quantity
            }
        }

        function calculatePricePerBox(tile) {
            if (tile.box.measurementUnit == 1 && !tile.qtyIsSqFt) {
                return tile.price * tile.box.quantity
            }

            if (tile.box.measurementUnit == 2 && tile.qtyIsSqFt) {
                return tile.price * tile.box.quantity
            }

            if (tile.box.measurementUnit == 1 && tile.qtyIsSqFt) {
                return (tile.quantity * tile.sqFt) * tile.box.quantity
            }
        }
    }
})();