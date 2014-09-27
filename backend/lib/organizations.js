'use strict';

/**
 * Module containing organization routes
 * @author CodeForBirmingham
 * @module backend/lib/organizations
 */

var config = require('./../config/config'),
    express = require('express'),
    router = express.Router();

function dummyResponse(req, res, next) {
    console.log(req.params.year);
    res.status(501);
    res.json({type: 'dummy', message: 'Not yet implemented'});
}

module.exports = function (db) {
    /**
     * @api {get} /:year/organizations Get Organizations
     * @apiName GetOrganizations
     * @apiGroup Organizations
     *
     * @apiParam {Date} year
     *
     * @apiDescription Get a list of all organization information.
     */
    router.get('/:year/organizations', dummyResponse);


    /**
     * @api {get} /:year/organizations/:ids Get Specific Organization
     * @apiName GetSpecificOrganizations
     * @apiGroup Organizations
     *
     * @apiParam {Date} year
     * @apiParam {String} ids single or comma separated list of ids.
     *
     * @apiDescription Get information on a specific or comma separated list of organization ids.
     */
    router.get('/:year/organizations/:ids', dummyResponse);

    /**
     * @api {get} /:year/organizations/:ids/transactions Get Specific Organizations Transactions
     * @apiName GetSpecificOrganizationsTransactions
     * @apiGroup Organizations
     *
     * @apiParam {Date} year
     * @apiParam {String} ids single or comma separated list of ids.
     *
     * @apiDescription Get a JSON Object containing several lists of organization transactions (mapped by organization id).
     */
    router.get('/:year/organizations/:ids/transactions', dummyResponse);

    /**
     * @api {get} /:year/organizations/:ids/transactions/:type Get Specific Organizations Transactions By Type
     * @apiName GetSpecificOrganizationsTransactionsByType
     * @apiGroup Organizations
     *
     * @apiParam {Date} year
     * @apiParam {String} ids single or comma separated list of ids.
     * @apiParam {String} type One of four possible transaction types (cash, inkind, receipt, expenditure);
     *
     * @apiDescription Get a JSON Object containing several lists of organization transactions (mapped by organization id).
     */
// TODO: Decide if this and transactions/ should be :type or explicit (type is more convenient, but less pretty for transactions/
    router.get('/:year/organizations/:ids/transactions/:type', dummyResponse);

    /**
     * @api {get} /:year/organizations/:ids/payees Get Specific Organizations Payees
     * @apiName GetSpecificOrganizationsPayees
     * @apiGroup Organizations
     *
     * @apiParam {Date} year
     * @apiParam {String} ids single or comma separated list of ids.
     *
     * @apiDescription Get a JSON Object containing several lists of organization payees (mapped by organization id).
     */
    router.get('/:year/organizations/:ids/payees', dummyResponse);

    /**
     * @api {get} /:year/organizations/:ids/contributors Get Specific Organizations Contributors
     * @apiName GetSpecificOrganizationsContributors
     * @apiGroup Organizations
     *
     * @apiParam {Date} year
     * @apiParam {String} ids single or comma separated list of ids.
     *
     * @apiDescription Get a JSON Object containing several lists of organization contributors (mapped by organization id).
     */
    router.get('/:year/organizations/:ids/contributors', dummyResponse);

    /**
     * @api {get} /:year/organizations/featured Get Featured Organizations
     * @apiName GetFeaturedOrganizations
     * @apiGroup Organizations
     *
     * @apiParam {Date} year
     *
     * @apiDescription Get information on featured organizations.
     */
    router.get('/:year/organizations/featured', dummyResponse);

    /**
     * @api {get} /:year/organizations/candidates Get Candidates
     * @apiName GetCandidates
     * @apiGroup Organizations
     *
     * @apiParam {Date} year
     *
     * @apiDescription Get information on all available candidates.
     */
    router.get('/:year/organizations/candidates', dummyResponse);

    /**
     * @api {get} /:year/organizations/candidates/featured Get Featured Candidates
     * @apiName GetFeaturedCandidates
     * @apiGroup Organizations
     *
     * @apiParam {Date} year
     *
     * @apiDescription Get information on featured candidates.
     */
    router.get('/:year/organizations/candidates/featured', dummyResponse);

    /**
     * @api {get} /:year/organizations/committees Get Committees
     * @apiName GetCommittees
     * @apiGroup Organizations
     *
     * @apiParam {Date} year
     *
     * @apiDescription Get information on all available committees.
     */
    router.get('/:year/organizations/committees', dummyResponse);

    /**
     * @api {get} /:year/organizations/committees/featured Get Featured Committees
     * @apiName GetFeaturedCommittees
     * @apiGroup Organizations
     *
     * @apiParam {Date} year
     *
     * @apiDescription Get information on featured committees.
     */
    router.get('/:year/organizations/committees/featured', dummyResponse);

    return router;
};

