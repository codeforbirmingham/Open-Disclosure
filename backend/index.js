/* 

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

app.use('/api', require('./config/routes'));

var server = app.listen(config.http.port, function () {
    console.log('Server listening on port: ' + config.http.port); 
});
