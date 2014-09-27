/*
    Setup API routes in an express Router object and export it.
 */

var config = require('./config'),
    express = require('express'),
    router = express.Router();

function dummyResponse(req, res, next) {
    console.log(req.params.year);
    res.status(501);
    res.json({type: 'dummy', message: 'Not yet implemented'});
}

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
 * @apiDescription Get information on a specific or comma separated list of organization ids..
 */
router.get('/:year/organizations/:ids', dummyResponse);

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


module.exports = router;
