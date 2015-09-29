(function () {
    'use strict';

    angular
        .module('app.news')
        .factory('catalogSvc', ['$http', 'appSettings', catalogSvc]);

    function catalogSvc($http, appSettings) {

        return {
            getCatalogs: getCatalogs
        };

        function getCatalogs() {
            //return catalogsMock();
            return $http.get(appSettings.serverPath + 'news/catalogs');
        }

        function catalogsMock(){
            return[
                {
                    id:1,
                    image:'/static/img/initial/news/catalog/News-In-Stock-Catalog-2015-Granada-Tile.jpg',
                    name:'Instock Catalog 2015'
                },
                {
                    id:2,
                    image:'/static/img/initial/news/catalog/News-Echo-Collection-Mini-Catalog-Granada-Tile.jpg',
                    name:'Echo Collection Mini Catalog'
                },
                {
                    id:3,
                    image:'/static/img/initial/news/catalog/News-Look-Book-2015-Granada-Tile.jpg',
                    name:'Instock Catalog 2015'
                },
                {
                    id:4,
                    image:'/static/img/initial/news/catalog/News-Look-Book-2013-Granada-Tile.jpg',
                    name:'Lookbook 2013'
                },
                {
                    id:5,
                    image:'/static/img/initial/news/catalog/News-Look-Book-2013-vol2-Granada-Tile.jpg',
                    name:'Lookbook 2013 - Volume 2'
                },
                {
                    id:6,
                    image:'/static/img/initial/news/catalog/News-Look-Book-2012-Granada-Tile.jpg',
                    name:'Lookbook 2012 - Volume 1'
                }
            ]
        }
    }
}());
