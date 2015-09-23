(function () {
    'use strict';

    angular
        .module('app.news')
        .factory('articleSvc', ['$http', 'appSettings', articleSvc]);

    function articleSvc($http, appSettings) {

        return {
            getArticles: getArticles
        };

        function getArticles() {
            return articlesMock();
        }

        function articlesMock(){
            return[
                {
                    id:1,
                    image:'/static/img/initial/news/article/Magazine-Affar-Granada-Tile-Cement.jpg',
                    title:'DESIGNING L.A.',
                    name:'AFAR',
                    description:'“The textures it creates are just amazing.” The Fez tile she used became Granada Tile’s\ ' +
                                'best seller after Bestor used it in Intelligentsia’s ﬁrst L.A. cafe.',
                    date:' 04-28-2015'
                },
                {
                    id:2,
                    image:'/static/img/initial/news/article/Magazine-Chatelaine-Granada-Tile.jpg',
                    title:'BOLD & FEARLESS',
                    name:'CHATELAINE ',
                    description:'PUT THE EMPHASIS ON FLOORS WITH PATTERNS. Commiting to a graphic ﬂoor tile takes guts,\ ' +
                                'but he payoﬀ is huge. Jessica chose a Morocco-inspired cement ﬂoor for this kitchen.',
                    date:' 04-28-2015'
                },
                {
                    id:3,
                    image:'/static/img/initial/news/article/Magazine-Coastal-Living-Granada-Tile.jpg',
                    title:'DESIGNING L.A.',
                    name:'AFAR',
                    description:'“The textures it creates are just amazing.” The Fez tile she used became Granada Tile’s\ ' +
                                'best seller after Bestor used it in Intelligentsia’s ﬁrst L.A. cafe.',
                    date:' 04-28-2015'
                },
                {
                    id:4,
                    image:'/static/img/initial/news/article/Magazine-Kitchen-Granada-Tile.jpg',
                    title:'BOLD & FEARLESS',
                    name:'CHATELAINE ',
                    description:'PUT THE EMPHASIS ON FLOORS WITH PATTERNS. Commiting to a graphic ﬂoor tile takes guts,\ ' +
                                'but he payoﬀ is huge. Jessica chose a Morocco-inspired cement ﬂoor for this kitchen.',
                    date:' 04-28-2015'
                },
                {
                    id:5,
                    image:'/static/img/initial/news/article/Magazine-Dwell-Granada-Tile.jpg',
                    title:'DESIGNING L.A.',
                    name:'AFAR',
                    description:'“The textures it creates are just amazing.” The Fez tile she used became Granada Tile’s\ ' +
                                'best seller after Bestor used it in Intelligentsia’s ﬁrst L.A. cafe.',
                    date:' 04-28-2015'
                },
                {
                    id:6,
                    image:'/static/img/initial/news/article/Magazine-HGTV-Granada-Tile.jpg',
                    title:'BOLD & FEARLESS',
                    name:'CHATELAINE ',
                    description:'PUT THE EMPHASIS ON FLOORS WITH PATTERNS. Commiting to a graphic ﬂoor tile takes guts,\ ' +
                                'but he payoﬀ is huge. Jessica chose a Morocco-inspired cement ﬂoor for this kitchen.',
                    date:' 04-28-2015'
                }
            ]
        }
    }
}());