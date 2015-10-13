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

        collectionsSvc.getGroup(pageSettings.groupId).then(function (response) {
            vm.group = response.data;
        });

        vm.labels = pageSettings.labels;

    }
}());
