$(document).ready(function () {
	// Dot blink for homepage
	(function () {
		var blink = 0;
		$('#yl-dot').heartbeat(500, function () {
			if (blink % 2 === 0) {
				$(this).css({ color: "#ee4000" });
			} else {
				$(this).css({ color: "#161A1F" });
			}
			blink += 1;
			blink %= 2;
		});
	})();
});
