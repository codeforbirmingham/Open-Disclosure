angular.module('openDisclosure')
  .controller('datavisCtrl', ['$scope', 'Api', function($scope, Api) {

    var initial = [23, 22, 21, 21, 23, 50, 102];
    $scope.circles = [];


    function initializeCircle() {
        var circle = d3.select("svg").selectAll("circle")
        .data(initial)
        .enter()
        .append("svg")
        .attr("cx", 230)
        .text(function(d){ return d; })
        .attr("cy", 230)
        .attr("r", function(d) {
          return d;
        })
        .style("fill", "red")
        .on("mouseover", function() {
          d3.select(this)
          .style("fill", "#67a1dd");
        })
        .on("mouseout", function() {
          d3.select(this)
          .style("fill", "green");
        });
    }

    initializeCircle();


  }]);
