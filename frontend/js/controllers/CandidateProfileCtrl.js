angular.module('openDisclosure')
.controller('candidateProfileCtrl', function ($scope, $routeParams, $http, $rootScope, $location) {
        
        $scope.candidate = $routeParams.candidate;
    });
