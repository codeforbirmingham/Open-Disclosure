angular.module('openDisclosure')
    .controller('candidatesCtrl', ['$scope', 'Api', function ($scope, Api) {
        Api.getCandidates().then(function (candidates) {
            $scope.candidates = candidates;
        });
    }]);

