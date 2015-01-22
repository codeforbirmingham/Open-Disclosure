angular.module('openDisclosure', [
    'ngRoute',
    'ui.bootstrap',
    'leaflet-directive',
    'config'

  ])
    .run(function ($rootScope, name, about, logo) {

        $rootScope.name = name;
        $rootScope.about = about;
        $rootScope.logo = logo;

    });