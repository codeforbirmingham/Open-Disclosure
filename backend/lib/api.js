'use strict';

/**
 * Module containing transactions routes
 * @module backend/lib/transactions
 */

var config = require('./../config/config'),
    express = require('express'),
    router = express.Router();

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

    return router;
};