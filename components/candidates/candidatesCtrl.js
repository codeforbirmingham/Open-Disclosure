angular.module('openDisclosure')
    .controller('candidatesCtrl', ['$scope', 'Api', function ($scope, Api) {
        $scope.sort = {
            name: false,
            office: false,
            contribution: false,
            expenditure: false
        };
        Api.getCandidates().then(function (candidates) {
            $scope.candidates = candidates;
        });
    }]);

