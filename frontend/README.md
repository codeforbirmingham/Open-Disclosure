Frontend
===============

__DO NOT__ commit the bower_components folder to version control!

Here is some information about getting setup to develop and deploy the frontend of Open-Disclosure.

## Installing Dependencies

In order for the application to work, we need to pull in the dependencies if we're setting up for the first time.

Dependencies in our frontend are managed by [Bower](http://bower.io). To get our dependencies, we'll first need to install Bower.

### Installing Bower

Installing Bower is super simple. Bower requires [node.js and npm](http://nodejs.org).

Install bower with npm like this:

```
npm install -g bower
```

Once we're done installing Bower, we can pull in our dependencies!

### Using Bower to Install Dependencies

Installing dependencies with Bower is super simple.

First, make sure that you're in the `frontend` directory. Once you've confirmed that, install the frontend dependencies by running:

```
bower install
```

That's it! You should now have all dependencies necessary to run the frontend of Open Disclosure.