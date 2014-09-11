angular.module('openDisclosure')
.config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'partials/home.html',
                controller: 'homeCtrl',
                controllerAs: 'homeCtrl'
            })
            .when('/candidate/:candidate', {
                templateUrl: 'partials/candidate-profile.html',
                controller: 'candidateProfileCtrl',
                controllerAs: 'candidateProfileCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
    });