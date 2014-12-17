$(document).ready(function () {
	var keyCodes = {
		'8': 'Backspace',
		'9': 'Tab',
		'13': 'Return',
		'16': 'S',
		'17': 'C',
		'18': 'M',
		'20': 'CapsLock',
		'27': 'Esc',
		'32': 'Space',
		'37': 'Left',
		'38': 'Up',
		'39': 'Right',
		'40': 'Down',
		'46': 'Delete'
	};
	
	$(document).keydown(function (event) {
		console.log(event.keyCode);
	});
});
