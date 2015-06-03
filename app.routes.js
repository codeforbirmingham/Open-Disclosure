angular.module('openDisclosure')
    .config(function ($routeProvider) {
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
            .otherwise({
                redirectTo: '/'
            });
    });
