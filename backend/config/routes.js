/*
    Setup API routes in an express Router object and export it.
 */

var config = require('./config'),
    express = require('express'),
    router = express.Router();

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

module.exports = router;
