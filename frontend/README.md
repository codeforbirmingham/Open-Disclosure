Frontend
===============

__DO NOT__ commit the bower_components folder to version control!

Here is some information about getting setup to develop and deploy the frontend of Open-Disclosure.

## Installing Dependencies

In order for the application to work, we need to pull in the dependencies if we're setting up for the first time.

Dependencies in our frontend are managed by [npm](https://www.npmjs.org/) and [Bower](http://bower.io).

### Installing Bower and Grunt tools

Installing Bower is super simple. Bower requires [node.js and npm](http://nodejs.org).

Install bower with npm like this:

```
npm install
```

Once we're done installing Bower, we can pull in our dependencies!

### Using Bower to Install Dependencies

Installing dependencies with Bower is super simple.

First, make sure that you're in the `frontend` directory. Once you've confirmed that, install the frontend dependencies by running:

```
bower install
```

That's it! You should now have all dependencies necessary to run the frontend of Open Disclosure.

## Preparing Your Environment

### Development

You can prepare a development environment by running this:

```
grunt dev
```

### Production

You can prepare a production environment by running this:

```
grunt dist
```

### Cleaning

You can clean your environment by running this:

```
grunt clean
```

## See Your Progress

You'll want to run a webserver on localhost to serve the files. The simplest way to do this is to run this from the frontend directory:

```
python -m SimpleHTTPServer
```

Now you can go to 0.0.0.0:8000 in a browser.
