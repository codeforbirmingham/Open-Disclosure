/**
 * App REST API Route settings.
 * @author CodeForBirmingham
 * @module backend/config/routes
 */

var config = require('./config'),
    express = require('express'),
    router = express.Router();

function dummyResponse(req, res, next) {
    console.log(req.params.year);
    res.status(501);
    res.json({type: 'dummy', message: 'Not yet implemented'});
}

module.exports = function (db) {
    /**
     * @api {get} / Get Service information
     * @apiName GetAppInfo
     * @apiGroup API
     *
     * @apiDescription Get basic information about the api.
     *
     * @apiSuccess {Object} JSON Object containing API information
     */
    router.get('/', function (req, res, next) {
        res.json(config.app);
    });

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

    /**
     * @api {get} /:year/transactions Get Transactions
     * @apiName GetTransactions
     * @apiGroup Transactions
     *
     * @apiParam {Date} year
     *
     * @apiDescription Get information on all available transactions.
     */
    router.get('/:year/transactions', dummyResponse);

    /**
     * @api {get} /:year/transactions/type/:type Get Contribution Transactions By Type
     * @apiName GetContributionTransactionsByType
     * @apiGroup Transactions
     *
     * @apiParam {Date} year
     * @apiParam {String} type One of four possible transaction types (cash, inkind, receipt, expenditure);
     *
     * @apiDescription Get information on all available cash contribution transactions.
     */
    router.get('/:year/transactions/type/:type', dummyResponse);

    /**
     * @api {get} /:year/transactions/:ids Get Specific Transactions
     * @apiName GetSpecificTransactions
     * @apiGroup Transactions
     *
     * @apiParam {Date} year
     * @apiParam {String} ids single or comma separated list of ids.
     *
     * @apiDescription Get information on a list of specific transactions.
     */
    router.get('/:year/transactions/:ids', dummyResponse);

    /**
     * @api {get} /:year/payees Get Payees
     * @apiName GetPayees
     * @apiGroup Payees
     *
     * @apiParam {Date} year
     *
     * @apiDescription Get information on all available payees.
     */
    router.get('/:year/payees', dummyResponse);

    /**
     * @api {get} /:year/payees/:ids Get Specific Payees
     * @apiName GetPayees
     * @apiGroup Payees
     *
     * @apiParam {Date} year
     * @apiParam {String} ids single or comma separated list of ids.
     *
     * @apiDescription Get information on specific payees.
     */
    router.get('/:year/payees/:ids', dummyResponse);

    /**
     * @api {get} /:year/contributors Get Contributors
     * @apiName GetContributors
     * @apiGroup Contributors
     *
     * @apiParam {Date} year
     *
     * @apiDescription Get information on all available payees.
     */
    router.get('/:year/contributors', dummyResponse);

    /**
     * @api {get} /:year/contributors/:ids Get Specific Contributors
     * @apiName GetSpecificContributors
     * @apiGroup Contributors
     *
     * @apiParam {Date} year
     * @apiParam {String} ids single or comma separated list of ids.
     *
     * @apiDescription Get information on specific contributors.
     */
    router.get('/:year/contributors/:ids', dummyResponse);

    /**
     * @api {get} /:year/districts Get Districts
     * @apiName GetDistricts
     * @apiGroup Districts
     *
     * @apiParam {Date} year
     *
     * @apiDescription Get information on all available districts.
     */
    router.get('/:year/districts', dummyResponse);

    /**
     * @api {get} /:year/districts/:ids Get Specific Districts
     * @apiName GetSpecificDistricts
     * @apiGroup Districts
     *
     * @apiParam {Date} year
     * @apiParam {String} ids single or comma separated list of ids.
     *
     * @apiDescription Get information on specific contributors.
     */
    router.get('/:year/districts/:ids', dummyResponse);

    return router;
}