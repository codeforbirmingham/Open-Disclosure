angular.module('openDisclosure')
    .controller('candidateCtrl', ['$scope', '$http', 'leafletData', function ($scope, $http, leafletData) {
        // leaflet doesn't play well with accordions: if the size or display property of
        // the leaflet container are changed, `invalidateSize()` has to be called on the
        // map instance.
        $scope.$watch('isCollapsed', function (value) {
            if (value === false) {
                leafletData.getMap('map-' + $scope.candidate.orgId).then(function (map) {
                    map.invalidateSize();
                });
            }
        });
        $http.get("assets/map/AL.geojson").success(function(data, status) {
            $scope.mapOutline = {
                data: data
            };
        });
    }]);


