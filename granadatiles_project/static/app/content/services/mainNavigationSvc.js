(function (){
	'use strict';

	angular
		.module('app.content')
		.factory('mainNavigationSvc', 
					['$http',
					 mainNavigationSvc]);

	function mainNavigationSvc($http) {

		return {
			getmainNavigation: getmainNavigation
		}

		function getmainNavigation(){
			return mainNavigationMock();
		}

		function mainNavigationMock(){
			return [
				{
					id:1,
					title:'Residential',
					image:'/static/img/initial/content/residential.png',
					description:'See examples of our cement tiles in kitchens, bathrooms, and outdoors. Normandy or Clunny',
					action:'View our Residential Installations'
				},
				{
					id:2,
					title:'Commercial',
					image:'/static/img/initial/content/commercial.png',
					description:'See examples of our cement tiles in kitchens, bathrooms, and outdoors. Normandy or Clunny',
					action:'View our commercial Installations'
				},
				{
					id:3,
					title:'In Stock',
					image:'/static/img/initial/content/in_stock.png',
					description:'See examples of our cement tiles in kitchens, bathrooms, and outdoors. Normandy or Clunny',
					action:'Shop in stock tiles - Available now!'
				},
				{
					id:4,
					title:'Custom',
					image:'/static/img/initial/content/custom.png',
					description:'See examples of our cement tiles in kitchens, bathrooms, and outdoors. Normandy or Clunny',
					action:'Shop custom tiles'
				}
			];
		}
	};

}());