/* 
    Main backend application driver, setup /api calls and
    serve static app content.
 */

var config = require('./config/config'),
    cors = require('cors'),
    morgan = require('morgan'),
    bodyParser = require('body-parser'),
    express = require('express'),
    mongoClient = require ('mongodb').MongoClient,
    app = express();

mongoClient.connect(config.mongo.url, function (err, db) {
    if (err) {
        throw err;
    }

    app.use(morgan('dev'));
    app.use(bodyParser.urlencoded({
        extended: true
    }));

    app.use('/', express.static(config.http.view));
    app.use('/api/docs', express.static(config.docs.view));
    app.use('/api/v1/', require('./config/routes')(db));

    var server = app.listen(config.http.port, function () {
        console.log('Server listening on port: ' + config.http.port);
    });
});