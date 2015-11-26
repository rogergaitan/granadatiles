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
            getSizes: getSizes,
            getStyles: getStyles,
            getTiles: getTiles,
            getMainTile:getMainTile,
            getInstallationPhoto: getInstallationPhoto
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

        function getStyles(groupId){
            return $http.get(appSettings.serverPath + 'groups/' + groupId + '/styles');
        }

        function getSizes(groupId){
            return $http.get(appSettings.serverPath + 'groups/' + groupId + '/sizes');
        }

        function getTiles(groupId){
            //return groupMock();
            return $http.get(appSettings.serverPath + 'groups/' + groupId + '/tiles')
        }

        function getMainTile(tileId){
            return $http.get(appSettings.serverPath + 'tiles/' + tileId)
        }

        function getInstallationPhoto(tileId){
            return $http.get(appSettings.serverPath + 'tiles/'+ tileId + '/installationphotos/')
        }

        function groupMock(){
            return[
                {
                    id:1,
                    name:'Kotka',
                    main:{
                        id:1,
                        name:'918 A',
                        image:'/static/img/initial/tiles/tiles/kotka.jpg',
                        discontinue:false,
                        new_item:false,
                        sizes:[
                            {
                                    id: 1,
                                    name: '6x6'
                                },
                                {
                                    id: 2,
                                    name: '8x8'
                                }
                        ]
                    },
                    tiles:[
                        {
                            id:2,
                            name:'918 B',
                            image:'/static/img/initial/tiles/tiles/Kotka918-B-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        },
                        {
                            id:3,
                            name:'918 C',
                            image:'/static/img/initial/tiles/tiles/Kotka918-C-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        },
                        {
                            id:4,
                            name:'918 D',
                            image:'/static/img/initial/tiles/tiles/Kotka918-D-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        }
                    ]
                },
                {
                    id:2,
                    name:'Aarhus',
                    main:{
                        id:5,
                        name:'813 A',
                        image:'/static/img/initial/tiles/tiles/aarhus.jpg',
                        discontinue:false,
                        new_item:false,
                        sizes:[
                            {
                                id: 1,
                                name: '8x8'
                            }
                        ]
                    },
                    tiles:[
                        {
                            id:6,
                            name:'813 B',
                            image:'/static/img/initial/tiles/tiles/Aarhus-813-B-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        },
                        {
                            id:7,
                            name:'813 C',
                            image:'/static/img/initial/tiles/tiles/Aarhus-813-C-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        },
                        {
                            id:8,
                            name:'813 D',
                            image:'/static/img/initial/tiles/tiles/Aarhus-813-D-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        }
                    ]
                },
                {
                    id:3,
                    name:'Avesta',
                    main:{
                        id:9,
                        image:'/static/img/initial/tiles/tiles/avesta.jpg',
                        discontinue:false,
                        new_item:false,
                        sizes:[
                            {
                                id: 1,
                                name: '8x8'
                            }
                        ]
                    },
                    tiles:[
                        {
                            id:10,
                            name:'800 B',
                            image:'/static/img/initial/tiles/tiles/Avesta-800-B-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        },
                        {
                            id:11,
                            name:'800 C',
                            image:'/static/img/initial/tiles/tiles/Avesta-800-C-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        },
                        {
                            id:12,
                            name:'800 D',
                            image:'/static/img/initial/tiles/tiles/Avesta-800-D-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        }
                    ]
                },
                {
                    id:4,
                    name:'Boden',
                    main:{
                        id:13,
                        name:'801 A',
                        image:'/static/img/initial/tiles/tiles/boden.jpg',
                        discontinue:false,
                        new_item:false,
                        sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                        ]
                    },
                    tiles:[
                        {
                            id:14,
                            name:'801 B',
                            image:'/static/img/initial/tiles/tiles/Boden-801-B-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        },
                        {
                            id:15,
                            name:'801 C',
                            image:'/static/img/initial/tiles/tiles/Boden-801-C-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        },
                        {
                            id:16,
                            name:'801 D',
                            image:'/static/img/initial/tiles/tiles/Boden-801-D-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        }
                    ]
                },
                {
                    id:5,
                    name:'Helsinki',
                    main:{
                        id:17,
                        name:'810 A',
                        image:'/static/img/initial/tiles/tiles/helsinki.jpg',
                        discontinue:false,
                        new_item:false,
                        sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                        ]
                    },
                    tiles:[
                        {
                            id:18,
                            name:'810 B',
                            image:'/static/img/initial/tiles/tiles/Helsinki-810-B-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        },
                        {
                            id:19,
                            name:'810 C',
                            image:'/static/img/initial/tiles/tiles/Helsinki-810-C-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        },
                        {
                            id:20,
                            name:'810 D',
                            image:'/static/img/initial/tiles/tiles/Helsinki-810-D-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        }
                    ]
                },
                {
                    id:6,
                    name:'Laholm',
                    main:{
                        id:21,
                        name:'802 A',
                        image:'/static/img/initial/tiles/tiles/laholm.jpg',
                        discontinue:false,
                        new_item:false,
                        sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                        ]
                    },
                    tiles:[
                        {
                            id:22,
                            name:'802 B',
                            image:'/static/img/initial/tiles/tiles/Laholm-802-B-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        },
                        {
                            id:23,
                            name:'802 C',
                            image:'/static/img/initial/tiles/tiles/Laholm-802-C-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        },
                        {
                            id:24,
                            name:'802 D',
                            image:'/static/img/initial/tiles/tiles/Laholm-802-D-Granada-Tile-Cement.jpg',
                            sizes:[
                                {
                                    id: 1,
                                    name: '8x8'
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }
}());