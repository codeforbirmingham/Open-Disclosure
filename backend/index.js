/* 
    Main backend application driver, setup /api calls and
    serve static app content.
 */

var config = require('./config/config'),
    cors = require('cors'),
    morgan = require('morgan'),
    bodyParser = require('body-parser'),
    express = require('express'),
    app = express();

app.use(morgan('dev'));
app.use(bodyParser.urlencoded({
    extended: true
}));


console.log(config.http.view);
app.use('/', express.static(config.http.view));
app.use('/api', require('./config/routes'));

var server = app.listen(config.http.port, function () {
    console.log('Server listening on port: ' + config.http.port);
});
