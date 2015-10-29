angular.module('openDisclosure')
  .controller('datavisCtrl', ['$scope', 'Api', function($scope, Api) {

    $scope.sortFields = [{
      name: 'name',
      label: 'Name'
    }, {
      name: 'office',
      label: 'Office'
    }, {
      name: 'contribution',
      label: 'Total Raised'
    }, {
      name: 'expenditure',
      label: 'Total Spent'
    }];
    $scope.curSortField = 'contribution';
    $scope.curSortOrderDesc = true;
    $scope.setSortField = function(sortField) {
      if ($scope.curSortField === sortField) {
        // Invert order.
        $scope.curSortOrderDesc = !$scope.curSortOrderDesc;
      } else {
        // Change sort field.
        $scope.curSortField = sortField;
        $scope.curSortOrderDesc = false;
      }
    };
    $scope.getOrderBy = function() {
      return $scope.curSortOrderDesc ? '-' + $scope.curSortField : $scope.curSortField;
    };

    function getSpentPercentage() {
      console.log('works');
      return "got percentage";
    }



    Api.getCandidates().then(function(candidates) {
      $scope.candidates = candidates;

      var svg = d3.select(document.getElementById("datavis"))
      .append("svg");
      .style('width', '100%');
      // Browser onresize event
      window.onresize = function() {
        $scope.$apply();
      };

      // hard-code data
      $scope.mockdata = [{
        name: "Greg",
        score: 98
      }, {
        name: "Ari",
        score: 96
      }, {
        name: 'Q',
        score: 75
      }, {
        name: "Loser",
        score: 48
      }];

      // Watch for resize event
            $scope.$watch(function() {
              return angular.element($window)[0].innerWidth;
            }, function() {
              $scope.render($scope.mockdata);
            });

            scope.render = function(data) {
              // our custom d3 code
            };


    });



  }]);
