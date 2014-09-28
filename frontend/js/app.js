angular.module('openDisclosure', ['ngRoute', 'config'])
    .run(function ($rootScope, name, about, logo) {

        $rootScope.name = name;
        $rootScope.about = about;
    });