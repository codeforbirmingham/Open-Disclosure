angular.module('openDisclosure')
    .controller('candidatesCtrl', ['$scope', 'Api', function ($scope, Api) {
        $scope.candidates = Api.getCandidates(2014);
        $scope.lastUpdate = "12/20/2014";
        $scope.searchParams = ["lastname","firstname", "totalSpent", "total spent (%)", "campaign"];
        $scope.isCollapsed = true;
        $scope.mapCenter = {
            lat: 32.91649,
            lng: -86.79199,
            zoom: 6
        };
   }]);


