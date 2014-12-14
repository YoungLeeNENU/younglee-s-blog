$(document).ready(function () {
	_minibuffer();
});

var _minibuffer = function () {
	_displayTime();
};

var _displayTime = function () {
	var changeTime = function () {
		var localTime = new Date(),
		    timeStr = localTime.toLocaleString();
		
		$('#L_time').text(timeStr);
		
		setTimeout(changeTime, 1000);
	};
	
	changeTime();
};
