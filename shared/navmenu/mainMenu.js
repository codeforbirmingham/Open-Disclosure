angular.module('openDisclosure')
    .directive('mainMenu', function () {
        return {
            restrict: 'E',
            templateUrl: 'shared/navmenu/mainMenu.html',
        }
    });