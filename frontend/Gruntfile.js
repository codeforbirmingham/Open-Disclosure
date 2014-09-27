module.exports = function (grunt) {

    grunt.initConfig({

        pkg: grunt.file.readJSON('package.json'),

        clean: [
            "build/",
            "annotated/",
            "index.html"
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
                    "libs/jquery/jquery.min.js",
                    "libs/bootstrap/dist/js/bootstrap.min.js",
                    "libs/angular/angular.min.js",
                    "libs/angular-route/angular-route.min.js",
                    "annotated/js/script.js",
                    "annotated/js/controllers/*.js",
                    "annotated/js/directives/*.js",
                    "annotated/js/factories/*.js",
                    "annotated/js/router.js"
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
        }

    });

    grunt.loadNpmTasks('grunt-ng-annotate');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-targethtml');

    grunt.registerTask('dev', ['targethtml:dev']);
    grunt.registerTask('dist', ['ngAnnotate', 'concat', 'uglify', 'targethtml:dist']);
}