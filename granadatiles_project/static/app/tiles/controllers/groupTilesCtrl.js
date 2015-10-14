(function () {
    'use strict';

    angular
        .module('app.tiles')
        .controller('groupTilesCtrl',
            ['pageSettings',
                'collectionsSvc',
                groupTilesCtrl]);

    function groupTilesCtrl(pageSettings, collectionsSvc) {
        var vm = this;

        collectionsSvc.getGroup().then(function (response){
            vm.group = response.data;
        });

        vm.labels = pageSettings.labels;

        vm.title = 'Designer Erin Adams';

        vm.description = 'The customizable Echo Tile Collection o?ers:\ ' +
            '•  Over 140 hand made cement tile designs •  Array of styles and sizes\ ' +
            '•  For residential projects (bathrooms, kitchens, patios and more\ ' +
            '•  For commercial projects (restaurants, cafes, hotels, spas, shops)\ ' +
            '•  For ?oors and walls';

    }
}());
