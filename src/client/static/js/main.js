"use strict";

require([
	// tools
	'jquery',
	'underscore',
	'backbone',
	// common
	'keyctrl',
	'heartbeat',
	'time',
	'cursor',
	// page
	'homepage'], function ($, _, Backbone) {
		console.log("我把试验性的一些想法放在这里，这个站点本身也是一个试验");
	});

require.config({
	baseUrl: "./static/js/tools/",    // 基础路径
	paths: {
		'jquery': "jquery-2.1.0.min",
		'underscore': "underscore-min",
		'backbone': "backbone-min",
		'keyctrl': "../common/keyctrl",
		'heartbeat': "../common/heartbeat",
		'time': "../common/time",
		'cursor': "../common/cursor",
		'homepage': "../page/homepage/homepage"
	},
	shim: {
		'underscore': {
			exports: '_'
		},
		'backbone': {
			deps: ['underscore', 'jquery'],
			exports: 'Backbone'
		},
		'heartbeat': {
			deps: ['jquery']
		},
		'time': {
			deps: ['jquery']
		},
		'cursor': {
			deps: ['jquery']
		},
		'homepage': {
			deps: ['jquery', 'underscore', 'backbone']
		}
	}
});
