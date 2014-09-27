'use strict';

/**
 * Main OpenDisclosure Express Driver
 * @author CodeForBirmingham
 * @module backend/index.js
 */

var config = require('./config/config'),
    cors = require('cors'),
    morgan = require('morgan'),
    bodyParser = require('body-parser'),
    express = require('express'),
    mongoClient = require ('mongodb').MongoClient,
    app = express();

/*
    Connect to MongoDB instance and pass db connection to API routes (and route sub modules), then proceed to start the
    express server.
 */
mongoClient.connect(config.mongo.url, function (err, db) {
    if (err) {
        throw err;
    }

    app.use(morgan('dev'));
    app.use(bodyParser.urlencoded({
        extended: true
    }));

    // Serve frontend static content
    app.use('/', express.static(config.http.view));

    // Load API Routes
    require('./config/api_routes')(app, db);

    var server = app.listen(config.http.port, function () {
        console.log('Server listening on port: ' + config.http.port);
    });

    /*
        Handle shutdown events to close db connection.
        Probably unnecessary, but could be useful if we need to add additional shutdown cleanup or logging.
     */
    process.on('SIGINT', function() {
        db.close();
        process.exit();
    });

    process.on('SIGTERM', function() {
        db.close();
        process.exit();
    });
});