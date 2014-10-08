'use strict';

/**
 * Module containing district routes
 * @author CodeForBirmingham
 * @module backend/lib/districts
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
};