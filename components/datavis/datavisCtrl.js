angular.module('openDisclosure')
  .controller('datavisCtrl', ['$scope', 'Api', function($scope, Api) {

    $scope.circle = initializeCircle();
    var initial = [23, 22, 21, 21, 23, 50, 102];

    function initializeCircle() {
      var initialcircle = d3.select("div")
        .append("svg")
        .attr("width", 70)
        .attr("height", 70)
        .append("circle")
        .attr("cx", 50)
        .attr("cy", 40)
        .attr("r", 20)
        .style("fill", "red")
        .on("mouseover", function() {
          d3.select(this)
          .style("fill", "#67a1dd");

        })
        .on("mouseout", function() {
          d3.select(this)
          .style("fill", "green");
        });
    };




  }]);
