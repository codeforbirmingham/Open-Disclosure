angular.module('openDisclosure')
    .controller('menuCtrl', ['$scope', '$location', '$modal', function ($scope, $location, $modal) {

                $scope.isActive = function (viewLocation) {
                    return viewLocation === $location.path();
                };

                //controls for modal
                $scope.open = function () {

                    $modal.open({
                        templateUrl: 'shared/aboutModal.html',
                        controller: 'modalCtrl'
                    });

                };
            }]);
