/*
    Config module for application wide information.
 */


var path = require('path'),
    config = {};

config.app = {
    name: 'OpenDisclosureBirmingham',
    description: 'This is an app'
};

config.http = {
    port: 8080,
    view: path.join(__dirname, '..', '..', 'frontend')
};

module.exports = config;
