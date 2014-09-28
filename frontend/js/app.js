angular.module('openDisclosure', ['ngRoute', 'config'])
    .run(function ($rootScope, name, about) {

        $rootScope.name = name;
        $rootScope.about = about;
    });