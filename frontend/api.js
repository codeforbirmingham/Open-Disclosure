angular.module('openDisclosure').factory('Api', function () {

    var Api = {};

    //GET /api/:year/organizations/
    Api.getOrganizations = function (year) {

    };

    //GET /api/:year/organizations/candidates/
    Api.getCandidates = function (year) {
        // Add computed grossGain and pctSpent to mock data.
        return mockData.map(function (candidate) {
            candidate.grossGain = candidate.cashContributions + candidate.inKindContributions;
            candidate.pctSpent = candidate.expenditures / candidate.grossGain * 100;
            return candidate;
        });
    };
    
    //GET /api/:year/organizations/committees/
    Api.getCommittees = function (year) {

    };

    //GET /api/:year/organizations/:id/
    Api.getOrganization = function (year, id) {

    };

    //GET /api/:year/organizations/candidates/featured
    Api.getFeaturedCandidates = function (year) {

    };

    //GET /api/:year/organizations/committees/featured
    Api.getFeaturedCommittees = function (year) {

    };

    //GET /api/:year/organizations/featured
    Api.getFeaturedOrganizations = function (year) {

    };

    //GET /api/:year/organizations/:id/contributors
    Api.getOrganizationContributors = function (year, id) {

    };

    //GET /api/:year/organizations/:id/payees
    Api.getOrganizationPayees = function (year, id) {

    };

    //GET /api/:year/organizations/:id/transactions
    Api.getOrganizationTransactions = function (year, id) {

    };

    //GET /api/:year/organizations/:id/transactions/:type
    Api.getOrganizationTransactions = function (year, id, type) {

    };

    //GET /api/:year/payees
    Api.getPayees = function (year) {

    };

    //GET /api/:year/transactions/
    Api.getTransactions = function (year) {

    };

    //GET /api/:year/transactions/:id
    Api.getTransaction = function (year) {

    };

    //GET /api/:year/transactions/type/:type
    Api.getTransactions = function (year, type) {

    };

    return Api;
});

var mockData = [
        {
            orgId: 1,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Richard Shelby",
            poll: 86
        },
        {
            orgId: 2,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Robert Bentley",
            poll: 92
        },
        {
            orgId: 3,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Jeff Sessions",
            poll: 21
        },
        {
            orgId: 4,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Luther Strange",
            poll: 65
        },
        {
            orgId: 5,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Jim Hubbard",
            poll: 32
        },
        {
            orgId: 6,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Gary Palmner",
            poll: 65
        },
        {
            orgId: 7,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Bob Reiley",
            poll: 65
        },
        {
            orgId: 8,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "George Wallace",
            poll: 65
        },
        {
            orgId: 9,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Condoleeza Rice",
            poll: 65
        }
    ];