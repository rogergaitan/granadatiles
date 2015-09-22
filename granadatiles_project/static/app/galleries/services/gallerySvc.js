(function () {
    'use strict';

    angular
        .module('app.galleries')
        .factory('gallerySvc',['$http','appSettings', gallerySvc]);

    function gallerySvc($http, appSettings) {

        return {
            getGalleries: getGalleries
        };

        function getGalleries() {
            return galleriesMock();
            //return $http.get(appSettings.serverPath + 'galleries');
        }

        function galleriesMock(){
            return [
                {
                    id:1,
                    name:'Residential Cement Tile',
                    image:'/static/img/initial/galleries/Installation-Residential-Cement-Tile-Granada-Tile-Cement.jpg',
                    categories:[
                        {
                            id:1,
                            name:'Kitchen'
                        },
                        {
                            id:2,
                            name:'BathRoom'
                        },
                        {
                            id:3,
                            name:'Living Room'
                        },
                        {
                            id:4,
                            name:'Outdoors'
                        }
                    ]
                },
                {
                    id:2,
                    name:'Commercial Cement Tile',
                    image:'/static/img/initial/galleries/Installation-Commercial-Cement-Tile-Granada-Tile-Cement.jpg',
                    categories:[
                        {
                            id:5,
                            name:'Restaurant'
                        },
                        {
                            id:6,
                            name:'Café'
                        },
                        {
                            id:7,
                            name:'Resort & Hotel'
                        },
                        {
                            id:8,
                            name:'Retail Office'
                        }
                    ]
                },
                {
                    id:3,
                    name:'Collection',
                    image:'/static/img/initial/galleries/Installation-Collection-Cement-Tile-Granada-Tile-Cement.jpg',
                    categories:[
                        {
                            id:9,
                            name:'Echo Tile Collection'
                        },
                        {
                            id:10,
                            name:'Minis Tile Collection'
                        },
                        {
                            id:11,
                            name:'Mauresque Tile Collection'
                        }
                    ]
                },
                {
                    id:4,
                    name:'United Stated Cities',
                    image:'/static/img/initial/galleries/Installation-United-States-Cement-Tile-Granada-Tile-Cement.jpg',
                    categories:[
                        {
                            id:12,
                            name:'Chicago'
                        },
                        {
                            id:13,
                            name:'Los Angeles'
                        }
                    ]
                },
                {
                    id:4,
                    name:'Historic Tile Installations',
                    image:'/static/img/initial/galleries/Installation-Historic-Tiles-Cement-Tile-Granada-Tile-Cement.jpg',
                    categories:[
                        {
                            id:14,
                            name:'America'
                        },
                        {
                            id:15,
                            name:'Europa'
                        },
                        {
                            id:16,
                            name:'Asia'
                        }
                    ]
                }

            ]
        }

    }

}());