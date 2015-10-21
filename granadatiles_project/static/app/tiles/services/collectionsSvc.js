(function () {
    'use strict';

    angular
        .module('app.tiles')
        .factory('collectionsSvc',
                ['appSettings',
                 '$http',
                collectionsSvc]);

    function collectionsSvc(appSettings, $http) {
        
        return {
            getCollections: getCollections,
            getMenuCollections: getMenuCollections,
            getFeaturedCollections: getFeaturedCollections,
            getCollection: getCollection,
            getCollectionGroups: getCollectionGroups,
            getFilteredMenuCollection: getFilteredMenuCollection,
            getGroup: getGroup,
            getTile: getTile
        };

        function getCollections() {
            return $http.get(appSettings.serverPath + 'collections');
        }

        function getMenuCollections(){
            return $http.get(appSettings.serverPath + 'collections/menu');
        }

        function getFilteredMenuCollection(collectionId){
             return $http.get(appSettings.serverPath + 'collections/menu/?exclude='+ collectionId);
        }

        function getFeaturedCollections() {
            return $http.get(appSettings.serverPath + 'collections/featured');
        }

        function getCollection(collectionId){
            return $http.get(appSettings.serverPath + 'collections/'+ collectionId);
        }

        function getCollectionGroups(collectionId) {
            return $http.get(appSettings.serverPath + 'collections/'+ collectionId + '/groups');
        }

        function getGroup(groupId) {
            return $http.get(appSettings.serverPath + 'groups/'+ groupId);
        }

        function getTile(groupId){
            return $http.get(appSettings.serverPath + 'groups/' + groupId + '/tiles')
        }

        /*function groupMock(){
            return[
                {
                    id:1,
                    title:'Kotka 918 A',
                    subtitle:'CUSTOM: 6” x 6” • 10” x 10”',
                    image:'/static/img/initial/tiles/tile/Kotka.jpg',
                    discontinue:false,
                    new:false,
                    others_style:[
                        {
                            id:1,
                            title:'918 B',
                            image:'/static/img/initial/tiles/tile/Kotka918-B-Granada-Tile-Cement.jpg'
                        },
                        {
                            id:2,
                            title:'918 C',
                            image:'/static/img/initial/tiles/tile/Kotka918-C-Granada-Tile-Cement.jpg'
                        },
                        {
                            id:3,
                            title:'918 D',
                            image:'/static/img/initial/tiles/tile/Kotka918-D-Granada-Tile-Cement.jpg'
                        }
                    ]
                },
                {
                    id:2,
                    title:'Aarhus 813 A',
                    subtitle:'IN STOCK: 8”x 8”',
                    image:'/static/img/initial/tiles/tile/Aarhus.jpg',
                    discontinue:false,
                    new:false,
                    others_style:[
                        {
                            id:1,
                            title:'813 B',
                            image:'/static/img/initial/tiles/tile/Aarhus-813-B-Granada-Tile-Cement.jpg'
                        },
                        {
                            id:2,
                            title:'813 C',
                            image:'/static/img/initial/tiles/tile/Aarhus-813-C-Granada-Tile-Cement.jpg'
                        },
                        {
                            id:3,
                            title:'813 D',
                            image:'/static/img/initial/tiles/tile/Aarhus-813-D-Granada-Tile-Cement.jpg'
                        }
                    ]
                },
                {
                    id:3,
                    title:'Avesta 800 A',
                    subtitle:'IN STOCK: 8”x 8”',
                    image:'/static/img/initial/tiles/tile/Avesta.jpg',
                    discontinue:false,
                    new_item:false,
                    others_style:[
                        {
                            id:1,
                            title:'800 B',
                            image:'/static/img/initial/tiles/tile/Avesta-800-B-Granada-Tile-Cement.jpg'
                        },
                        {
                            id:2,
                            title:'800 C',
                            image:'/static/img/initial/tiles/tile/Avesta-800-C-Granada-Tile-Cement.jpg'
                        },
                        {
                            id:3,
                            title:'800 D',
                            image:'/static/img/initial/tiles/tile/Avesta-800-D-Granada-Tile-Cement.jpg'
                        }
                    ]
                },
                {
                    id:4,
                    title:'Boden 801 A',
                    subtitle:'IN STOCK: 8”x 8”',
                    image:'/static/img/initial/tiles/tile/Boden.jpg',
                    discontinue:false,
                    new_item:false,
                    others_style:[
                        {
                            id:1,
                            title:'801 B',
                            image:'/static/img/initial/tiles/tile/Boden-801-B-Granada-Tile-Cement.jpg'
                        },
                        {
                            id:2,
                            title:'801 C',
                            image:'/static/img/initial/tiles/tile/Boden-801-C-Granada-Tile-Cement.jpg'
                        },
                        {
                            id:3,
                            title:'801 D',
                            image:'/static/img/initial/tiles/tile/Boden-801-D-Granada-Tile-Cement.jpg'
                        }
                    ]
                },
                {
                    id:5,
                    title:'Helsinki 810 A',
                    subtitle:'IN STOCK: 8”x 8”',
                    image:'/static/img/initial/tiles/tile/Helsinki.jpg',
                    discontinue:false,
                    new_item:false,
                    others_style:[
                        {
                            id:1,
                            title:'810 B',
                            image:'/static/img/initial/tiles/tile/Helsinki-810-B-Granada-Tile-Cement.jpg'
                        },
                        {
                            id:2,
                            title:'810 C',
                            image:'/static/img/initial/tiles/tile/Helsinki-810-C-Granada-Tile-Cement.jpg'
                        },
                        {
                            id:3,
                            title:'810 D',
                            image:'/static/img/initial/tiles/tile/Helsinki-810-D-Granada-Tile-Cement.jpg'
                        }
                    ]
                },
                {
                    id:6,
                    title:'Laholm 802 A',
                    subtitle:'IN STOCK: 8”x 8”',
                    image:'/static/img/initial/tiles/tile/Laholm.jpg',
                    discontinue:false,
                    new_item:false,
                    others_style:[
                        {
                            id:1,
                            title:'802 B',
                            image:'/static/img/initial/tiles/Laholm-802-B-Granada-Tile-Cement.jpg'
                        },
                        {
                            id:2,
                            title:'802 C',
                            image:'/static/img/initial/tiles/Laholm-802-C-Granada-Tile-Cement.jpg'
                        },
                        {
                            id:3,
                            title:'802 D',
                            image:'/static/img/initial/tiles/Laholm-802-D-Granada-Tile-Cement.jpg'
                        }
                    ]
                }
            ]
        }*/

        
    }
}());