/**
 * @fileOverview Page Time Display
 * @name time.js
 * @author YoungLee youngleemails@gmail.com
 * @license MIT
 */

$(document).ready(function () {
	$('#minibuffer .time').pseudoheartbeat(1000, function () {
		// Construct
		var timer = new Date(),
			date = timer.toLocaleDateString(),    // for spare
			time = timer.getHours() + ":" + timer.getMinutes() + ":" + timer.getSeconds();    // for spare
		
		$(this).text(timer.toLocaleString());
		
		// Deconstruct
		timer = null;
	});
});
