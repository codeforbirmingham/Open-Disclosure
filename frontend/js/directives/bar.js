angular.module('openDisclosure')
.directive('navigation', function() {
  return {
      restrict: 'E',
      transclude: true,
      templateUrl: 'partials/navigation.html'
  };
});
