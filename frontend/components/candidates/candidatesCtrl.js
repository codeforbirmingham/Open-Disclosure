angular.module('openDisclosure')
    .controller('candidatesCtrl', ['$scope', 'Api', function ($scope, Api) {
        $scope.candidates = Api.getCandidates(2014);
        $scope.lastUpdate = "12/20/2014";
        $scope.grossGain = function(candidates) {
            cash  = this.cashContributions;
            inKind = this.inKindContributions;
            return cash + inKind;
        };
        $scope.pctSpent = function () {
            return candidate.expenditures / this.grossGain * 100;
        };
        
        $scope.searchParams = ["lastname","firstname", "totalSpent", "total spent (%)", "campaign"];
        $scope.isCollapsed= true;
    
        
    }]);


