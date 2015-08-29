angular.module('openDisclosure')
  .controller('candidatesCtrl', ['$scope', 'Api', function($scope, Api) {
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
      if ($scope.curSortField == sortField) {
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
    Api.getCandidates().then(function(candidates) {
      $scope.candidates = candidates;
    });
    $scope.spent = function (contribution, expenditure) {
        return {
        width : (100 * (expenditure / (contribution + expenditure))) + "%"
        };
    };

  }]);
