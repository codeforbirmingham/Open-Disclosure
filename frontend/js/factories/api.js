angular.module('openDisclosure').factory('Api', function () {
    
    var Api = {};
    
    //GET /api/:year/organizations/
    Api.getOrganizations = function(year) {
        
    };
    
    //GET /api/:year/organizations/candidates/
    Api.getCandidates = function(year) {
        
    };
    
    //GET /api/:year/organizations/committees/
    Api.getCommittees = function(year) {
        
    };
    
    //GET /api/:year/organizations/:id/
    Api.getOrganization = function(year, id) {
        
    };
    
    //GET /api/:year/organizations/candidates/featured
    Api.getFeaturedCandidates = function(year) {
        
    };
    
    //GET /api/:year/organizations/committees/featured
    Api.getFeaturedCommittees = function(year) {
        
    };
    
    //GET /api/:year/organizations/featured
    Api.getFeaturedOrganizations = function(year) {
        
    };
    
    //GET /api/:year/organizations/:id/contributors
    Api.getOrganizationContributors = function(year, id) {
        
    };
    
    //GET /api/:year/organizations/:id/payees
    Api.getOrganizationPayees = function(year, id) {
        
    };
    
    //GET /api/:year/organizations/:id/transactions
    Api.getOrganizationTransactions = function(year, id) {
        
    };
    
    //GET /api/:year/organizations/:id/transactions/:type
    Api.getOrganizationTransactions = function(year, id, type) {
        
    };
    
    //GET /api/:year/payees
    Api.getPayees = function(year) {
        
    };
    
    //GET /api/:year/transactions/
    Api.getTransactions = function(year) {
        
    };
    
    //GET /api/:year/transactions/:id
    Api.getTransaction = function(year) {
        
    };
    
    //GET /api/:year/transactions/type/:type
    Api.getTransactions = function(year, type) {
        
    };
    
    return Api;
});