angular.module('openDisclosure')
    .controller('candidatesCtrl', ['$scope', '$http', 'Api', function ($scope, $http, Api) {
        $scope.candidates = Api.getCandidates(2014);
        $scope.lastUpdate = "12/20/2014";
        $scope.searchParams = ["lastname","firstname", "totalSpent", "total spent (%)", "campaign"];
        $scope.isCollapsed= true;
        angular.extend($scope, {
            center: {
                lat: 33.5250,
                lng: -86.8130,
                zoom: 5
            }
        });
        $http.get("assets/map/AL.geojson").success(function(data, status) {
            angular.extend($scope, {
                geojson: {
                    data: data
                }
            });
        });
    }]);


