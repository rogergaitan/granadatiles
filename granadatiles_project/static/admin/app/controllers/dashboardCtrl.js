(function () {
    'use strict';

    angular
        .module('app')
        .controller('dashboardCtrl', dashboardCtrl);

    dashboardCtrl.$inject = ['dashboardSvc', 'angularSvcWrappers']; 

    function dashboardCtrl(dashboardSvc, angularSvcWrappers) {
        /* jshint validthis:true */
        var vm = this;
        dashboardSvc.getItemsCount().then(function (response) {
            vm.itemsCount = response.data;
        });

        dashboardSvc.getLatestUser().then(function (response) {
            vm.lastestUsers = response.data;
        });

        dashboardSvc.getGroupsbycollectionChartData().then(function (response) {
            var pieChartCanvas = angularSvcWrappers.$("#pieChart").get(0).getContext("2d");
            var pieChart = new angularSvcWrappers.Chart(pieChartCanvas);
            vm.PieData = response.data;
            var pieOptions = {
                //Boolean - Whether we should show a stroke on each segment
                segmentShowStroke: true,
                //String - The colour of each segment stroke
                segmentStrokeColor: "#fff",
                //Number - The width of each segment stroke
                segmentStrokeWidth: 1,
                //Number - The percentage of the chart that we cut out of the middle
                percentageInnerCutout: 50, // This is 0 for Pie charts
                //Number - Amount of animation steps
                animationSteps: 100,
                //String - Animation easing effect
                animationEasing: "easeOutBounce",
                //Boolean - Whether we animate the rotation of the Doughnut
                animateRotate: true,
                //Boolean - Whether we animate scaling the Doughnut from the centre
                animateScale: false,
                //Boolean - whether to make the chart responsive to window resizing
                responsive: true,
                // Boolean - whether to maintain the starting aspect ratio or not when responsive, if set to false, will take up entire container
                maintainAspectRatio: false,

            };
            //Create pie or douhnut chart
            // You can switch between pie and douhnut using the method below.  
            pieChart.Doughnut(vm.PieData, pieOptions);
        });

    }
})();
