angular.module('openDisclosure')
    .controller('aboutModalCtrl', ['$scope', '$modal', '$modalInstance', function ($scope, $modal, $modalInstance) {
        $scope.close = function() {
            $modalInstance.close();
        };
    }]);
