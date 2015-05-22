"use strict";

require(['jquery', 'underscore', 'backbone'], function ($, _, Backbone) {
	//TODO: 
});

require.config({
	baseUrl: "./tools/",    // 基础路径
	paths: {
		'jquery': "jquery-2.1.0.min",
		'underscore': "underscore-min",
		'backbone': "backbone-min"
	},
	shim: {
		'underscore': {
			exports: '_'
		},
		'backbone': {
			deps: ['underscore', 'jquery'],
			exports: 'Backbone'
		}
	}
});
