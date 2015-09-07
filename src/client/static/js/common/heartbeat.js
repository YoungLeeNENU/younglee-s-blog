/**
 * @fileOverview bind heartbeat operations for Young Lee's personal network
 * @name heartbeat.js
 * @author Yong Lee yongleemails@gmail.com
 * @license GPL V3
 */
define(function (heartbeat) {
    (function($) {
        /**
         * Use setTimeout to setup a heart beat operation.
         * @param { Number } interval: milliseconds
         * @param { Function } callback: callback function
         * @param { Boolean } optbreak: [optianl parameter] condition to stop heart beat
         * @returns { jQuery Object } Caller
         */
        $.fn.heartbeat = function (interval, callback, optbreak) {
            var context = this;
            var _setHeartBeat = function () {
                var timer = undefined;

                callback.call(context);
                timer = setTimeout(_setHeartBeat, interval);
                if (optbreak != undefined && timer != undefined) {
                    clearTimeout(timer);
                    timer = null;
                }
            };

            _setHeartBeat();

            return this;
        };

        $.heartbeat = function (interval, callback, optbreak) {
            var _setHeartBeat = function () {
                var timer = undefined;

                callback();
                timer = setTimeout(_setHeartBeat, interval);
                if (optbreak != undefined && timer != undefined) {
                    clearTimeout(timer);
                    timer = null;
                }            
            };

            _setHeartBeat();
        };

        /**
         * Use setTimeout to make one heart beat.
         * @param { Number } interval: milliseconds
         * @param { Function } callback: callback function
         * @returns { jQuery Object } Caller
         */
        $.fn.delay = function (interval, callback) {
            var context = this,
                timer = undefined;

            timer = setTimeout(function () {
                callback.call(context);
                clearTimeout(timer);
                timer = null;
            }, interval);

            return this;
        };

        /**
         * Use setInterval to make one pseudo heart beat.
         * @param { Number } interval: milliseconds
         * @param { Function } callback: callback function
         * @param { Boolean } optbreak: [optianl parameter] condition to stop heart beat
         * @returns { jQuery Object } Caller
         */
        $.fn.pseudoheartbeat = function (interval, callback, optbreak) {
            var context = this,
                timer = undefined;

            var cb = function () {
                callback.call(context);
            };

            callback.call(context);
            timer = setInterval(function () {
                callback.call(context);
            }, 1000);
            if (optbreak != undefined && timer != undefined) {
                clearInterval(timer);
                timer = null;
            }

            return this;
        };
    })(jQuery);
});
