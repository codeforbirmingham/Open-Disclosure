'use strict';

/**
 * Module containing payee routes
 * @author CodeForBirmingham
 * @module backend/lib/payees
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

    return router;
};