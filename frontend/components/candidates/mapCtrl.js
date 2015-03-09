angular.module('openDisclosure')
    .controller('mapCtrl', ['$scope', '$http', 'leafletData', function ($scope, $http, leafletData) {
        $scope.mapCenter = {
            lat: 32.91649,
            lng: -86.79199,
            zoom: 6
        };
        $http.get("assets/map/AL.geojson").success(function(data, status) {
            $scope.mapOutline = {
                data: data
            };
        });
    }]);


