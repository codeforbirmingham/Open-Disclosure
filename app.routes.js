angular.module('openDisclosure')
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'components/home/home.html',
                controller: 'homeCtrl',
                controllerAs: 'homeCtrl'
            })
            .when('/candidates', {
                templateUrl: 'components/candidates/candidates.html',
                controller: 'candidatesCtrl',
                controllerAs: 'candidatesCtrl'
            })
            .when('/visualize', {
                templateUrl: 'components/datavis/datavis.html',
                controller: 'datavisCtrl',
                controllerAs: 'datavisCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
    }]);
