angular.module('openDisclosure')
    .controller('candidateProfileCtrl', function ($scope, $routeParams, $http, $rootScope, $location) {

        $scope.thingToRequest = $routeParams.candidate;
        //make request to server
        
        //put results in this variable
        $scope.candidate = {
            name : "Test Name",
            contributions: 100000,
            expenditures: 50000,
            count: 1234
        };

        
    });