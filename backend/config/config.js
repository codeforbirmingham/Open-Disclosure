/**
 * Configuration module for app wide information
 * @author CodeForBirmingham
 * @module backend/config/routes
 */

var path = require('path'),
    config = {};

config.app = {
    name: 'OpenDisclosureBirmingham',
    description: 'This is an app'
};

config.api = {
    base: '/api'
};

config.http = {
    port: 8080,
    view: path.join(__dirname, '..', '..', 'frontend')
};

config.docs = {
    route: '/docs',
    view: path.join(__dirname, '..', 'apidocs')
};

config.mongo = {
    url: 'mongodb://127.0.0.1:27017/open-disclosure'
};

module.exports = config;
