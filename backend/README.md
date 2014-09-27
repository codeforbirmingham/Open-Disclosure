# OpenDisclosure Backend

Responsible for hosting static of the frontend content on '/', as well as api routes on /api/. 

API documentation can be found at '/api/docs'. If it isn't loading, make the documentation folder is named 'apidocs' and
that the apidocs have been generated.

## Setup

Setup should be relatively straight forward. First, modify the config file located at 'config/config.js' and update 
it according for your HTTPS and APNS/GCM certs, DB Credentials, etc. To install dependencies:

```
npm install
```

To run the service:
```
sudo node server.js
```

## Generating Documentation

Currently, the RheumPRO promis server uses jsdoc for module documentation, and apidoc for REST API documentation. 

To generate documentation, you'll need jsdoc and apidoc from npm:
```
sudo npm install -g jsdoc apidoc
```
To generate REST API documentation (generated from route.js):
```
apidoc -i config/ -o apidocs/
```

To view it for local use, first install http-server:
```
sudo npm install -g http-server
```

Then simply execute it in the docs or apidocs directory:
```
cd apidocs/
http-server
```

And connect to localhost:8080 to view the documentation.

Alternatively, you can just start the server and view the apps at 'yourserver.com/api/docs'.