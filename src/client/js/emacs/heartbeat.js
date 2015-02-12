/**
 * @fileOverview bind heartbeat operations for Young Lee's personal network
 * @name heartbeat.js
 * @author Yong Lee yongleemails@gmail.com
 * @license GPL V3
 */
(function($) {
	/**
	 * Use setTimeout to setup a heart beat operation
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
			if (optbreak != undefined && timer != undefined)
				clearTimeout(timer);
		};
		
		_setHeartBeat();
		
		return this;
	};
})(jQuery);
