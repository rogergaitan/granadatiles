(function () {
    'use strict';

    angular
        .module('app.galleries')
        .factory('gallerySvc',['$http', gallerySvc]);

    function gallerySvc($http) {

        return {
            getSection: getSection,
            getGalleries: getGalleries
        }

        function getGalleries(sectionId) {
            return galleriesMock(sectionId);
        }

        function getSection(sectionId) {
            return getMockSection(sectionId);
        }

        function getMockSection() {
            return {
                image:'/static/img/initial/content/banner-photos-cement-Granada-Tile-Cement.jpg',
                title: '<h1>Photos of Cement & Concrete Tile Installations</h1>',
                description: "Granada Tile is pleased to share photos of some of the cement tile installations using " +
                "our ﬂagship Echo Collection tiles. Our hand made cement and concrete tiles have been used in private " +
                "residences and commercial projects, indoors and outdoors, and on ﬂoors and on walls (and even on ceilings). " +
                "These cement and concrete tile installation photos feature bathroom tile, kitchen tile, tile backslashes, " +
                "wall tiles, ﬂoor tiles, commercial tiles, restaurant tiles, spa tiles, and patio tiles. "
            }
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
                            name:'Kitchen',
                            image:{
                                title:'Badajoz Adds a Graphic Jolt to a Portland Kitchen',
                                description:'Our friends at Jessica Helgerson Interior Design used our Badajoz cement ' +
                                            'tile design in the remodeled kitchen of a Portland, Oregon, condominium. ' +
                                            'The bold black-and-white concrete tile installation harmonizes with the strong ' +
                                            'lines of the rest of the space. Em Shephard was the project manager. ' +
                                            'Photograph by Lincoln Barbour/courtesy Jessica Helgerson Interior Design.',
                                image:'/static/img/initial/galleries/Essential-Shapes-Granada-Tile-Cement.jpg',
                                designer:'Bestor Architecture '
                            }
                        },
                        {
                            id:2,
                            name:'BathRoom',
                            image:{
                                title:'Badajoz Adds a Graphic Jolt to a Portland Kitchen',
                                description:'Our friends at Jessica Helgerson Interior Design used our Badajoz cement ' +
                                            'tile design in the remodeled kitchen of a Portland, Oregon, condominium. ' +
                                            'The bold black-and-white concrete tile installation harmonizes with the strong ' +
                                            'lines of the rest of the space. Em Shephard was the project manager. ' +
                                            'Photograph by Lincoln Barbour/courtesy Jessica Helgerson Interior Design.',
                                image:'/static/img/initial/galleries/Essential-Shapes-Granada-Tile-Cement.jpg',
                                designer:'Bestor Architecture '
                            }
                        },
                        {
                            id:3,
                            name:'Living Room',
                            image:{
                                title:'Badajoz Adds a Graphic Jolt to a Portland Kitchen',
                                description:'Our friends at Jessica Helgerson Interior Design used our Badajoz cement ' +
                                            'tile design in the remodeled kitchen of a Portland, Oregon, condominium. ' +
                                            'The bold black-and-white concrete tile installation harmonizes with the strong ' +
                                            'lines of the rest of the space. Em Shephard was the project manager. ' +
                                            'Photograph by Lincoln Barbour/courtesy Jessica Helgerson Interior Design.',
                                image:'/static/img/initial/galleries/Essential-Shapes-Granada-Tile-Cement.jpg',
                                designer:'Bestor Architecture '
                            }
                        },
                        {
                            id:4,
                            name:'Outdoors',
                            image:{
                                title:'Badajoz Adds a Graphic Jolt to a Portland Kitchen',
                                description:'Our friends at Jessica Helgerson Interior Design used our Badajoz cement ' +
                                            'tile design in the remodeled kitchen of a Portland, Oregon, condominium. ' +
                                            'The bold black-and-white concrete tile installation harmonizes with the strong ' +
                                            'lines of the rest of the space. Em Shephard was the project manager. ' +
                                            'Photograph by Lincoln Barbour/courtesy Jessica Helgerson Interior Design.',
                                image:'/static/img/initial/galleries/Essential-Shapes-Granada-Tile-Cement.jpg',
                                designer:'Bestor Architecture '
                            }
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
                            name:'Restaurant',
                            image:{
                                title:'Badajoz Adds a Graphic Jolt to a Portland Kitchen',
                                description:'Our friends at Jessica Helgerson Interior Design used our Badajoz cement ' +
                                            'tile design in the remodeled kitchen of a Portland, Oregon, condominium. ' +
                                            'The bold black-and-white concrete tile installation harmonizes with the strong ' +
                                            'lines of the rest of the space. Em Shephard was the project manager. ' +
                                            'Photograph by Lincoln Barbour/courtesy Jessica Helgerson Interior Design.',
                                image:'/static/img/initial/galleries/Essential-Shapes-Granada-Tile-Cement.jpg',
                                designer:'Bestor Architecture '
                            }
                        },
                        {
                            id:6,
                            name:'Café',
                            image:{
                                title:'Badajoz Adds a Graphic Jolt to a Portland Kitchen',
                                description:'Our friends at Jessica Helgerson Interior Design used our Badajoz cement ' +
                                            'tile design in the remodeled kitchen of a Portland, Oregon, condominium. ' +
                                            'The bold black-and-white concrete tile installation harmonizes with the strong ' +
                                            'lines of the rest of the space. Em Shephard was the project manager. ' +
                                            'Photograph by Lincoln Barbour/courtesy Jessica Helgerson Interior Design.',
                                image:'/static/img/initial/galleries/Essential-Shapes-Granada-Tile-Cement.jpg',
                                designer:'Bestor Architecture '
                            }
                        },
                        {
                            id:7,
                            name:'Resort & Hotel',
                            image:{
                                title:'Badajoz Adds a Graphic Jolt to a Portland Kitchen',
                                description:'Our friends at Jessica Helgerson Interior Design used our Badajoz cement ' +
                                            'tile design in the remodeled kitchen of a Portland, Oregon, condominium. ' +
                                            'The bold black-and-white concrete tile installation harmonizes with the strong ' +
                                            'lines of the rest of the space. Em Shephard was the project manager. ' +
                                            'Photograph by Lincoln Barbour/courtesy Jessica Helgerson Interior Design.',
                                image:'/static/img/initial/galleries/Essential-Shapes-Granada-Tile-Cement.jpg',
                                designer:'Bestor Architecture '
                            }
                        },
                        {
                            id:8,
                            name:'Retail Office',
                            image:{
                                title:'Badajoz Adds a Graphic Jolt to a Portland Kitchen',
                                description:'Our friends at Jessica Helgerson Interior Design used our Badajoz cement ' +
                                            'tile design in the remodeled kitchen of a Portland, Oregon, condominium. ' +
                                            'The bold black-and-white concrete tile installation harmonizes with the strong ' +
                                            'lines of the rest of the space. Em Shephard was the project manager. ' +
                                            'Photograph by Lincoln Barbour/courtesy Jessica Helgerson Interior Design.',
                                image:'/static/img/initial/galleries/Essential-Shapes-Granada-Tile-Cement.jpg',
                                designer:'Bestor Architecture '
                            }
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
                            name:'Echo Tile Collection',
                            image:{
                                title:'Badajoz Adds a Graphic Jolt to a Portland Kitchen',
                                description:'Our friends at Jessica Helgerson Interior Design used our Badajoz cement ' +
                                            'tile design in the remodeled kitchen of a Portland, Oregon, condominium. ' +
                                            'The bold black-and-white concrete tile installation harmonizes with the strong ' +
                                            'lines of the rest of the space. Em Shephard was the project manager. ' +
                                            'Photograph by Lincoln Barbour/courtesy Jessica Helgerson Interior Design.',
                                image:'/static/img/initial/galleries/Essential-Shapes-Granada-Tile-Cement.jpg',
                                designer:'Bestor Architecture '
                            }
                        },
                        {
                            id:10,
                            name:'Minis Tile Collection',
                            image:{
                                title:'Badajoz Adds a Graphic Jolt to a Portland Kitchen',
                                description:'Our friends at Jessica Helgerson Interior Design used our Badajoz cement ' +
                                            'tile design in the remodeled kitchen of a Portland, Oregon, condominium. ' +
                                            'The bold black-and-white concrete tile installation harmonizes with the strong ' +
                                            'lines of the rest of the space. Em Shephard was the project manager. ' +
                                            'Photograph by Lincoln Barbour/courtesy Jessica Helgerson Interior Design.',
                                image:'/static/img/initial/galleries/Essential-Shapes-Granada-Tile-Cement.jpg',
                                designer:'Bestor Architecture '
                            }
                        },
                        {
                            id:11,
                            name:'Mauresque Tile Collection',
                            image:{
                                title:'Badajoz Adds a Graphic Jolt to a Portland Kitchen',
                                description:'Our friends at Jessica Helgerson Interior Design used our Badajoz cement ' +
                                            'tile design in the remodeled kitchen of a Portland, Oregon, condominium. ' +
                                            'The bold black-and-white concrete tile installation harmonizes with the strong ' +
                                            'lines of the rest of the space. Em Shephard was the project manager. ' +
                                            'Photograph by Lincoln Barbour/courtesy Jessica Helgerson Interior Design.',
                                image:'/static/img/initial/galleries/Essential-Shapes-Granada-Tile-Cement.jpg',
                                designer:'Bestor Architecture '
                            }
                        }
                    ]
                },
                {
                    id:4,
                    name:'United Stated Cities ',
                    image:'/static/img/initial/galleries/Installation-United-States-Cement-Tile-Granada-Tile-Cement.jpg',
                    categories:[
                        {
                            id:12,
                            name:'Chicago',
                            image:{
                                title:'Badajoz Adds a Graphic Jolt to a Portland Kitchen',
                                description:'Our friends at Jessica Helgerson Interior Design used our Badajoz cement ' +
                                            'tile design in the remodeled kitchen of a Portland, Oregon, condominium. ' +
                                            'The bold black-and-white concrete tile installation harmonizes with the strong ' +
                                            'lines of the rest of the space. Em Shephard was the project manager. ' +
                                            'Photograph by Lincoln Barbour/courtesy Jessica Helgerson Interior Design.',
                                image:'/static/img/initial/galleries/Essential-Shapes-Granada-Tile-Cement.jpg',
                                designer:'Bestor Architecture '
                            }
                        },
                        {
                            id:13,
                            name:'Los Angeles',
                            image:{
                                title:'Badajoz Adds a Graphic Jolt to a Portland Kitchen',
                                description:'Our friends at Jessica Helgerson Interior Design used our Badajoz cement ' +
                                            'tile design in the remodeled kitchen of a Portland, Oregon, condominium. ' +
                                            'The bold black-and-white concrete tile installation harmonizes with the strong ' +
                                            'lines of the rest of the space. Em Shephard was the project manager. ' +
                                            'Photograph by Lincoln Barbour/courtesy Jessica Helgerson Interior Design.',
                                image:'/static/img/initial/galleries/Essential-Shapes-Granada-Tile-Cement.jpg',
                                designer:'Bestor Architecture '
                            }
                        }
                    ]
                }

            ]
        }

    }

}());