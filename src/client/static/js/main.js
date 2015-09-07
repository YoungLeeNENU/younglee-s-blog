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
        console.log('Copyright Young Lee 2015 youngleemails@gmail.com');
    });

require.config({
    baseUrl: "static/js/",    // 基础路径
    paths: {
        'jquery': "tools/jquery-2.1.0.min",
        'underscore': "tools/underscore-min",
        'backbone': "tools/backbone-min",
        'keyctrl': "common/keyctrl",
        'heartbeat': "common/heartbeat",
        'time': "common/time",
        'cursor': "common/cursor",
        'homepage': "page/homepage/homepage"
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
