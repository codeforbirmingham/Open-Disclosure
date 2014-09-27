/**
 * App REST API Route settings.
 * @author CodeForBirmingham
 * @module backend/config/api_routes
 */

var config = require('./config'),
    express = require('express'),
    router = express.Router();

module.exports = function (app, db) {
    app.use('/api/docs', express.static(config.docs.view));



    // Load API Router Modules
    app.use('/api', require('./../lib/api')(db));
    app.use('/api', require('./../lib/contributors')(db));
    app.use('/api', require('./../lib/districts')(db));
    app.use('/api', require('./../lib/organizations')(db));
    app.use('/api', require('./../lib/payees')(db));
    app.use('/api', require('./../lib/transactions')(db));

};