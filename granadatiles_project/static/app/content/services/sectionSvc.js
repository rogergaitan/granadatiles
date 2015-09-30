(function() {
    'use strict';

    angular
        .module('app.content')
        .factory('sectionSvc', ['$http','appSettings', sectionSvc]);


    function sectionSvc($http, appSettings) {

        return {
            getSection: getSection,
            getCover: getCover
        };

        function getCover(sectionId) {
            return $http.get(appSettings.serverPath + 'sections/' + sectionId + '/cover');;
        }

        function getSection(sectionId) {
            //return getMockSection(sectionId);
            return $http.get(appSettings.serverPath + 'sections/' + sectionId );
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

        //TODO API api/section/:sectionId/cover
        function getMockCover() {
            return {
                image: '/static/img/initial/content/Cluny-on-bath-Granada-tile-cement.jpg',
                designer: 'Ryan Phillips',
                photographer: 'Deindre Doherty',
                featuredArticle: {
                    title:'Bath of the Month Oct 2013',
                    image:'/static/img/initial/news/House-Beautiful-Granada-Tile-cement.png',
                    url:''
                },
                articles:[
                    {
                        url:'http://www.dwell.com/',
                        magazineName:'Dwell',
                        magazineLogo:'/static/img/initial/news/Dwell-Granada-Tile-cement.png'
                    },
                    {
                        url:'http://www.coastalliving.com/',
                        magazineName:'Martha Living',
                        magazineLogo:'/static/img/initial/news/Martha-Living-Granada-Tile-cement.png'
                    },
                    {
                        url:'http://www.revistaad.es/',
                        magazineName:'AD',
                        magazineLogo:'/static/img/initial/news/AD-Granada-Tile-cement.png'
                    },
                    {
                        url:'http://www.elledecor.com/',
                        magazineName:'Elle Decor',
                        magazineLogo:'/static/img/initial/news/Elle-Decor-Granada-Tile-cement.png'
                    }
                ]
            }
        }
    }
})();