angular.module('openDisclosure')
    .controller('candidatesCtrl', ['$scope', 'Api', function ($scope, Api) {
    
        $scope.candidates = Api.getCandidates(2014);
        console.log($scope.candidates);
    }]);