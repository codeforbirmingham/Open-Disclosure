angular.module('openDisclosure')
    .controller('candidatesCtrl', ['$scope', 'Api', function ($scope, Api) {
        $scope.candidates = Api.getCandidates(2014);
        $scope.lastUpdate = "12/20/2014";
        $scope.searchParams = ["lastname","firstname", "totalSpent", "total spent (%)", "campaign"];
        $scope.isCollapsed = true;
        $scope.mapCenter = {
            lat: 33.5250,
            lng: -86.8130,
            zoom: 5
        };
   }]);


