'use strict';

/**
 * Module containing transactions routes
 * @author CodeForBirmingham
 * @module backend/lib/transactions
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

    return router;
};