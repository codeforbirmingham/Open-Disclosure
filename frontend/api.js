angular.module('openDisclosure').factory('Api', function () {

    var Api = {};

    //GET /api/:year/organizations/
    Api.getOrganizations = function (year) {

    };

    //GET /api/:year/organizations/candidates/
    Api.getCandidates = function (year) {
        return mockData;
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
            name: "Test Candidate1"
        },
        {
            orgId: 2,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Test Candidate2"
        },
        {
            orgId: 3,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Test Candidate3"
        },
        {
            orgId: 4,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Test Candidate4"
        },
        {
            orgId: 5,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Test Candidate5"
        },
        {
            orgId: 6,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Test Candidate6"
        },
        {
            orgId: 7,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Test Candidate7"
        },
        {
            orgId: 8,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Test Candidate8"
        },
        {
            orgId: 9,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Test Candidate9"
        },
        {
            orgId: 10,
            position: "My Position",
            district: "My District",
            cashContributions: 200000,
            expenditures: 100000,
            inKindContributions: 100000,
            name: "Test Candidate10"
        },
    ];