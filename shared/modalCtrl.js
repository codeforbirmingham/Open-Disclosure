angular.module('openDisclosure')
    .controller('modalCtrl', ['$scope', '$modal', '$modalInstance', function ($scope, $modal, $modalInstance) {
        $scope.close = function() {
            $modalInstance.close();
        };
    }]);
