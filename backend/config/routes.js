/*

 */

var config = require('./config'),
    express = require('express'),
    router = express.Router();

router.get('/', function (req, res, next) {
    res.json(config.app);
});

module.exports = router;
