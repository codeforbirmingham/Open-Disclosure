angular.module('openDisclosure')
    .config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'partials/home.html',
                controller: 'homeCtrl',
                controllerAs: 'homeCtrl'
            })
            .when('/candidates', {
                templateUrl: 'partials/candidates.html',
                controller: 'candidatesCtrl',
                controllerAs: 'candidatesCtrl'
            })
            .when('/committees', {
                templateUrl: 'partials/committees.html',
                controller: 'committeesCtrl',
                controllerAs: 'committeesCtrl'
            })
            .when('/contributors', {
                templateUrl: 'partials/contributors.html',
                controller: 'contributorsCtrl',
                controllerAs: 'contributorsCtrl'
            })
            .when('/stats', {
                templateUrl: 'partials/stats.html',
                controller: 'statsCtrl',
                controllerAs: 'statsCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
    });