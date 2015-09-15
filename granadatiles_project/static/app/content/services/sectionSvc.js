(function() {
    'use strict';

    angular
        .module('app.content')
        .factory('sectionSvc', ['pageSettings',
            sectionSvc
        ]);


    function sectionSvc(pageSettingsSvc) {

        return {
            getSection: getSection,
            getCover: getCover
        };

        function getCover(sectionId) {
            if (sectionId == 1)
                return getMockCover(sectionId);
            else return {};

        }

        function getSection(sectionId) {
            return getMockSection(sectionId);
        }

        //TODO API api/section/:id
        function getMockSection() {
            return {
                title: '<h1>Tiles in my Portfolio</h1>',
                description: "My Portfolio is the home for all of your favorite tiles from across the Granada Tile collections. Don't go hunting through \
                            the website to try to find that one special tile you loved; save it to your Portfolio. Have you created a really great custom \
                            colorway tile in the Echo Collection Catalogue? Don't lose your work; save it to your Portfolio. Want to do a room layout? \
                            Use the tiles in your Portfolio to experiment with different combinations."
            }
        };

        //TODO API api/section/:sectionId/covers
        function getMockCover() {
            return {
                image: '/static/img/initial/content/Cluny-on-bath-Granada-tile-cement.jpg',
                designer: 'Ryan Phillips',
                photographer: 'Deindre Doherty',
            }
        };
    }
})();