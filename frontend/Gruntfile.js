module.exports = function (grunt) {

    grunt.initConfig({

        pkg: grunt.file.readJSON('package.json'),

        clean: [
            "build/",
            "annotated/",
            "index.html",
            "config.js"
        ],

        ngAnnotate: {
            acmApp: {
                files: [
                    {
                        expand: true,
                        src: [
                            "js/**/*.js"
                        ],
                        rename: function (dest, src) {
                            return 'annotated/' + src;
                        }
                    },
                ],
            },
        },

        concat: {
            options: {
                mangle: false
            },
            dist: {
                src: [
                    "assets/libs/bootstrap/dist/js/bootstrap.min.js",
                    "assets/libs/angular/angular.min.js",
                    "assets/libs/angular-route/angular-route.min.js",
                    "assets/libs/angular-leaflet-directive/dist/angular-leaflet-directive.min.js",
                    "assets/libs/angular-bootstrap/ui-bootstrap-tpls.min.js",
                    "annotated/js/app.js",
                    "annotated/js/controllers/*.js",
                    "annotated/js/directives/*.js",
                    "annotated/js/factories/*.js",
                    "annotated/js/modules/*.js",
                ],
                dest: 'build/js/production.js',
            }
        },

        uglify: {
            build: {
                src: 'build/js/production.js',
                dest: 'build/js/production.min.js'
            }
        },

        targethtml: {
            dev: {
                files: {
                    'index.html': 'index.template'
                }
            },
            dist: {
                files: {
                    'index.html': 'index.template'
                }
            }
        },

        ngconstant: {
            options: {
                dest: 'config.js',
                name: 'config',
            },
            dist: {
                constants: 'config.json'
            }
        },

    });

    grunt.loadNpmTasks('grunt-ng-annotate');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-targethtml');
    grunt.loadNpmTasks('grunt-ng-constant');

    grunt.registerTask('dev', ['ngconstant', 'targethtml:dev']);
    grunt.registerTask('dist', ['ngconstant', 'ngAnnotate', 'concat', 'uglify', 'targethtml:dist']);
}