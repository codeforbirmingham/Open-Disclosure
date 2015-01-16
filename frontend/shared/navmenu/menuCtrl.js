angular.module('openDisclosure')
    .controller('menuCtrl', ['$scope', '$location', '$modal', function ($scope, $location, $modal) {
            
                $scope.isActive = function (viewLocation) {
                    return viewLocation === $location.path();
                };

                //controls for modal
                $scope.open = function () {

                    var modalInstance = $modal.open({
                        templateUrl: 'shared/aboutModal.html',
                        controller: 'modalCtrl',
                        resolve: {
                            items: function () {
                                return $scope.items;
                            }
                        }
                    });
                    
                 $scope.close = function() {
                     $modal.close();
                 };

                };
            }]);