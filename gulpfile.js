'use strict';
var path = require('path');
var gulp = require('gulp');
var scss = require('gulp-scss');
var haml = require('gulp-haml');
var prettify = require('gulp-prettify');

var files = {
	style: {
		src: path.join(__dirname, 'src/client/static/scss/**/*.scss'),
		dest: path.join(__dirname, 'src/client/static/css')
	},
	template: {
		src: path.join(__dirname, 'src/client/templates/haml/*.haml'),
		dest: path.join(__dirname, 'src/client/templates/html')
	}
};

gulp.task('style', function(){
    return gulp.src(files.style.src)
		.pipe(scss())
        .pipe(gulp.dest(files.style.dest));
}).task('template', function () {
	return gulp.src(files.template.src)
		.pipe(haml())
		.pipe(prettify())
		.pipe(gulp.dest(files.template.dest));
});

gulp.task('default', ['style', 'template']);

gulp.task('watch', ['default']);
