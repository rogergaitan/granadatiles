(function () {
    'use strict';

    angular
        .module('app.content')
        .controller('videoCtrl',['videoSvc','sectionSvc',videoCtrl]);

    function videoCtrl(videoSvc, sectionSvc) {
        var vm = this;

        vm.title = 'Tile Videos - How to Tile Videos from Granada Tile ';

        vm.breadcrumds = 'News / Press';


        vm.description = '<p>Ever wondered how cement tiles are made? Take a peak behind the scenes at this remarkable\ ' +
                        'technique developed a century and a half ago. This tile video shows you the steps in the process\ ' +
                        'from creating a custom metal design mold to curing and packing the tiles.</p><p>Need some guidance\ ' +
                        'on how to install your tile? Coming soon: handy tile installation videos. These tile videos will\ ' +
                        'give you step-by-step audiovisual instructions and tips to make tile installation a breeze. Cant\ ' +
                        'wait? Dont miss the installation instructions available with each of the product collections.</p>\<' +
                        'p>Video - Granada Tile Revives the Fine Art of Making Cement Tile</p>\<' +
                        'p>Granada Tile creates sensational, handmade, eco-friendly cement and concrete tiles. We work\ ' +
                        'closely with architects and designers on their resorts, spas, restaurants, stores, and o?ce\ ' +
                        'projects. Homeowners and interior designers have chosen Granada Tile for their kitchens, bathrooms,\ ' +
                        'living rooms, pools, and patios on ?oors and walls. </p> <p>Our Echo Collection uses a technique\ ' +
                        'developed in France in the late 1870s. The key elements are the plate, the crown, the lid, the design\ ' +
                        'mold, the ladle, and the press. In addition to a vast collection of historic bronze design molds,\ ' +
                        'Granada Tile also make new molds constantly so clients can match their tile to their style. </p>\<' +
                        'p>Each area of each tile is handpoured. We have bestsellers that we keep in stock. We also do custom\ ' +
                        'tiles. Clients use our online Echo Collection Catalog to color their tiles.</p>\ ' +
                        '<p>Each tile is pressed to 2,000 PSI. This fuses the layers and makes the tile very strong. The\ ' +
                        '?nished tile is 5/8" of an inch thick and the color layer is 1/8". Once the tile has cured,\ ' +
                        'it will be packed, shipped, and installed. The result is a ?oor or wall that will last a life time.</p>\<' +
                        'p>Because of the handmade process and natural ingredients, these tiles exude an organic beauty.\ ' +
                        'So go ahead. Fall in love...</p>';


        videoSvc.getVideos().then(function (response) {
            vm.videos = response.data;
        });



    }

}());