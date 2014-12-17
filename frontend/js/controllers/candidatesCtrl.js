angular.module('openDisclosure')
    .controller('candidatesCtrl', ['$scope', 'Api', function ($scope, Api) {
    
        $scope.candidates = Api.getCandidates(2014);
    }]);


