/**
 * @fileOverview handle keyboard events
 * @name keyboard.js
 * @author Young Lee youngleemails@gmail.com
 * @license GPL V3
 * C-f  cursor forward
 * C-b  cursor back
 * C-n  cursor next
 * C-p  cursor previous
 * C-l  set middle
 * C-v  screen forward
 * C-a  
 * C-e 
 * C-h
 * C-k
 * C-w
 * C-space
 * C-/
 * C-y
 * C-x C-b
 * M-x
 * M-f
 * M-b
 * M-v
 * M-a
 * M-e
 * M-<
 * M->
 * M-d
 */
(function($) {
	function EmacsKeyBind () {
		this._defaults = {
		};
		this._fixed = {
			'': {
			}
		};
		$.extend(this._default, this._fixed['']);
		this._disable = [];
	}

	$.extend(EmacsKeyBind.prototype, {
		'ctrl-keycode': 17,
		'meta-keycode': 18,
		'a-keycode': 65,
		'b-keycode': 66,
		'c-keycode': 67,
		'd-keycode': 68,
		'e-keycode': 69,
		'f-keycode': 70,		
		'g-keycode': 71,
		'h-keycode': 72,
		'i-keycode': 73,
		'j-keycode': 74,
		'k-keycode': 75,
		'l-keycode': 76,
		'm-keycode': 77,
		'n-keycode': 78,
		'o-keycode': 79,
		'p-keycode': 80,
		'q-keycode': 81,
		'r-keycode': 82,		
		's-keycode': 83,
		't-keycode': 84,
		'u-keycode': 85,
		'v-keycode': 86,
		'w-keycode': 87,
		'x-keycode': 88,
		'y-keycode': 89,
		'z-keycode': 90,
		'>-keycode': 190,
		'<-keycode': 188,
		'space-keycode': 32,
		'/-keycode': 191,
		command: {
			cursorForward: {    // C-f
				txt: 'C-f',
				showCmd: true,
				pending: false,
				type: 'Ctrl',
				keyStroke: {
					shortCutHead: 17,    // ctrl
					shortCutTail: 70    // f
				},
			}
		},
	});

	$.fn.emacsListenKeyBind = function (options) {
		
	};
	
	$.emacsListenKeyBind = new EmacsKeyBind();
	
})(jQuery);
