'use strict';

/**
 * Module containing contributor routes
 * @author CodeForBirmingham
 * @module backend/lib/contributors
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

    return router;
};