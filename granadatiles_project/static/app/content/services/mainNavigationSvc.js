(function (){
	'use strict';

	angular
		.module('app.content')
		.factory('mainNavigationSvc', 
					['$http',
                     'appSettings',
					 mainNavigationSvc]);

	function mainNavigationSvc($http, appSettings) {

		return {
			getmainNavigation: getmainNavigation
		}

		function getmainNavigation(){
		    return $http.get(appSettings.serverPath + 'index_navigation');
		}

	};

}());