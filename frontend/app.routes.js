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
            .when('/contributors', {
                templateUrl: 'components/contributors/contributors.html',
                controller: 'contributorsCtrl',
                controllerAs: 'contributorsCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
    });