angular.module('openDisclosure')
    .controller('candidateProfileCtrl', function ($scope, $routeParams, $http, $rootScope, $location) {

        $scope.thingToRequest = $routeParams.candidate;
        //make request to server
        
        //put results in this variable. This is test data
        $scope.candidate = {
            name : "Robert Bentley",
            contributions: 100000,
            expenditures: 50000,
            count: 1234,
            image: "http://governor.alabama.gov/assets/2013/08/Robert-Bentley.jpg",
            description: "Bentley was elected to the Alabama House of Representatives in 2002 and served a total of two four-year terms from 2002 to 2010. After term-limited Governor Bob Riley could not seek reelection, Bentley announced his intentions to run for the Republican nomination for Governor. Bentley won in a seven candidate primary and faced Democrat Ron Sparks, the outgoing Alabama Commissioner of Agriculture, in the general election.[3] Bentley received just over 58% of the statewide vote and won by a margin of over 230,000 votes--the largest margin recorded for a Republican in an open-seat race in Alabama history.",
            contributors: ['test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor', 'test contributor2', 'test contributor']
        };

        
    });