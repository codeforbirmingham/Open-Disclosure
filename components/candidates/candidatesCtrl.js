angular.module('openDisclosure')
    .controller('candidatesCtrl', ['$scope', 'Api', function ($scope, Api) {
        $scope.sortField = 'contribution';
        $scope.sortOrderDescending = true;
        $scope.setSortField = function (sortField) {
            if ($scope.sortField == sortField) {
                // Invert order.
                $scope.sortOrderDescending = !$scope.sortOrderDescending;
            } else {
                // Change sort field.
                $scope.sortField = sortField;
                $scope.sortOrderDescending = false;
            }
        };
        $scope.getOrderBy = function () {
            return $scope.sortOrderDescending ? '-' + $scope.sortField : $scope.sortField;
        };
        Api.getCandidates().then(function (candidates) {
            $scope.candidates = candidates;
        });
    }]);
