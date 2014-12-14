$(document).ready(function () {
	_minibuffer();
});

var _minibuffer = function () {
	_displayTime();
};

var _displayTime = function () {
	var _changeTime = function () {
		var localTime = new Date(),
		    timeStr = localTime.toLocaleString();
		
		$('#L_time').text(timeStr);
		
		setTimeout(_changeTime, 1000);
	};
	
	_changeTime();
};
