$(document).ready(function () {
	_miniBufTime();
});

var _miniBufTime = function () {
	$('#L_time').heartbeat(1000, function () {
		var localTime = new Date(),
		    timeStr = localTime.toLocaleString();
		
		$(this).text(timeStr);	
	});
};
