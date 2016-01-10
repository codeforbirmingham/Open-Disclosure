angular.module('openDisclosure')
    .controller("datavisCtrl", function ($scope, Api) {
        $scope.sortFields = [{
         name: 'name',
         label: 'Name'
    }, {
         name: 'office',
         label: 'Office'
    }, {
         name: 'district',
         label: 'District'
    }, {
        name: 'party',
        label: 'Party'  
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

        var expenses = [];
        $scope.labels = [];
        $scope.series = ['Raised', 'Spent'];
        $scope.data = [[],[]];
        $scope.onClick = function (points, evt) {
            console.log(points, evt);
        };
        Api.getCandidates().then(function (candidates) {

            $scope.candidates = candidates.slice(0, 5);
            $scope.candidates.forEach(function (e) {
                $scope.data[0].push(e.expenditure);
                $scope.data[1].push(e.contribution);
                $scope.labels.push(e.name);
            });
            console.log($scope.data);
        });
    });