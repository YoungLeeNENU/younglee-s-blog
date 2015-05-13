/**
 * @fileOverview key board click controls
 * @name keyctrl.js
 * @author Young Lee youngleemails@gmail.com
 * @license MIT
 */
(function () {
    var win = window;    // Browser only

	// keyCode 和键盘事件映射关系
    win.keyPrint = {
        //TODO: 支持小键盘区
        '9': { default: '    ', afterShift: '    ' },    // Tab
        '32': { default: ' ', afterShift: ' ' },
        '48': { default: '0', afterShift: ')' },
        '49': { default: '1', afterShift: '!' },
        '50': { default: '2', afterShift: '@' },
        '51': { default: '3', afterShift: '#' },
        '52': { default: '4', afterShift: '$' },
        '53': { default: '5', afterShift: '%' },
        '54': { default: '6', afterShift: '^' },
        '55': { default: '7', afterShift: '&' },
        '56': { default: '8', afterShift: '*' },
        '57': { default: '9', afterShift: '(' },
        '65': { default: 'a', afterShift: 'A' },
        '66': { default: 'b', afterShift: 'B' },
        '67': { default: 'c', afterShift: 'C' },
        '68': { default: 'd', afterShift: 'D' },
        '69': { default: 'e', afterShift: 'E' },
        '70': { default: 'f', afterShift: 'F' },
        '71': { default: 'g', afterShift: 'G' },
        '72': { default: 'h', afterShift: 'H' },
        '73': { default: 'i', afterShift: 'I' },
        '74': { default: 'j', afterShift: 'J' },
        '75': { default: 'k', afterShift: 'K' },
        '76': { default: 'l', afterShift: 'L' },
        '77': { default: 'm', afterShift: 'M' },
        '78': { default: 'n', afterShift: 'N' },
        '79': { default: 'o', afterShift: 'O' },
        '80': { default: 'p', afterShift: 'P' },
        '81': { default: 'q', afterShift: 'Q' },
        '82': { default: 'r', afterShift: 'R' },
        '83': { default: 's', afterShift: 'S' },
        '84': { default: 't', afterShift: 'T' },
        '85': { default: 'u', afterShift: 'U' },
        '86': { default: 'v', afterShift: 'V' },
        '87': { default: 'w', afterShift: 'W' },
        '88': { default: 'x', afterShift: 'X' },
        '89': { default: 'y', afterShift: 'Y' },
        '90': { default: 'z', afterShift: 'Z' },
        '186': { default: ';', afterShift: ':' },
        '187': { default: '=', afterShift: '+' },
        '188': { default: ',', afterShift: '<'},
        '189': { default: '-', afterShift: '_' },
        '190': { default: '.', afterShift: '>' },
        '191': { default: '/', afterShift: '?' },
        '192': { default: '`', afterShift: '~' },
        '219': { default: '[', afterShift: '{' },
        '220': { default: '\\', afterShift: '|' },
        '221': { default: ']', afterShift: '}' },
        '222': { default: '\'', afterShift: '"' }
    };
    win.keyCtrl = {
		'8': { action: Backspace },
        '13': { action: Enter },
        '16': { action: Shift },
        '17': { action: Ctrl },
        '18': { action: Alt },
        '20': { action: CapsLock },
        '27': { action: "Esc" },    //TODO: 后续支持?
        '33': { action: "PgUp" },    //TODO: 后续支持向上翻页
        '34': { action: "PgDn" },    //TODO: 后续支持向下翻页
        '35': { action: End },
        '36': { action: Home },
        '37': { action: Left },
        '38': { action: Up },
        '39': { action: Right },
        '40': { action: Down },
        '46': { action: "Delete" },    //TODO: 后续支持删除光标处的字母
        '92': { action: "WinRight" },    //TODO: 后续支持?
        '93': { action: "Menu" }    //TODO: 后续支持?
    };

	/**
	 * 击键类
	 * @param { Number } keycode 键盘事件得到的 keycode
	 * @returns { Constructor } Scope safe constructor
	 */
    function KeyClick(keycode) {
        if (this instanceof KeyClick) {
            this.keycode = keycode;
        } else {
            return new KeyClick();
        }
    }
    KeyClick.prototype = {
        constructor: KeyClick,
        dispatch: function () {
            if (this.keycode) {
                var strcode = String(this.keycode);
                if (win.keyPrint.hasOwnProperty(strcode)) {
                    var dft = win.keyPrint[strcode]["default"],
                        shifted = win.keyPrint[strcode]["afterShift"],
                        opt = {
							type: "print",
                            code: this.keycode,
                            dft: dft,
                            shifted: shifted,
							triggered: false
						};
                    
                    return new PrintKey(opt);
                } else if (win.keyCtrl.hasOwnProperty(strcode)) {
                    var action = win.keyCtrl[strcode]["action"];
                    
                    if (action instanceof Object) {
                        var opt = {
							type: "ctrl",
                            code: this.keycode,
                            action: action.constructor
						};
                        
                        return new action(opt);
                    } else if (typeof action === "string") {
                        var opt = {
                            type: "ctrl",
                            code: this.keycode,
                            action: action,
							triggered: false
                        };

                        return new PrintKey(opt);
                    } else {
                        return "nilCode";    // 没有对应的 keyCode
                    }
                } else {
                    return "nilCode";    // 没有对应的 keyCode
                }
            } else {
                return "nilCode";    // 没有对应的 keyCode
            }
        }
    };

	// 共享键盘事件队列和控制键队列的 KeyQueue 构造器
    var KeyQueue = (function () {
        var _keyqueue = [],    // Shared stack
			_ctrlqueue = [];    // queue for control keys
        
        function QueueCtrl() {
            if (this instanceof QueueCtrl) {
                //TODO: 
            } else {
                return new QueueCtrl();
            }
        }

        QueueCtrl.prototype = Object.create(KeyClick.prototype, {
			constructor: {
				configurable: true,
				enumerable: true,
				value: QueueCtrl,
				writable: true
			}
		});
		
		QueueCtrl.prototype.regist = function (jsonOpt) {
			_keyqueue.push(jsonOpt);
		};
		QueueCtrl.prototype.queueLog = function () {
			return _keyqueue;
		};

        return QueueCtrl;
    })();
	

	/**
	 * 打印类
	 * @param { Object } opt 选项信息
	 * @returns { Constructor } Scope safe constructor
	 */
    function PrintKey(opt) {
        if (this instanceof PrintKey) {
            this.opt = opt;
        } else { return new PrintKey(opt); }
    }
	PrintKey.prototype = new KeyQueue();
	PrintKey.prototype.constructor = PrintKey;
	PrintKey.prototype.test = function () {
        if (this.opt.type === "print") { console.log(this.opt.dft); }
		else { console.log(this.opt.action); }
    };
	

	/**
	 * Backspace 键
	 * @param { Object } opt 选项信息
	 * @returns { Constructor } Scope safe constructor
	 */
	function Backspace(opt) {
		if (this instanceof Backspace) {
			this.opt = opt;
		} else { return new Backspace(opt); }
	}
	Backspace.prototype = new KeyQueue();
	Backspace.prototype.test = function () {
		console.log("Backspace");
	};
	
	
	/**
	 * Enter 键
	 * @param { Object } opt 选项信息
	 * @returns { Constructor } Scope safe constructor
	 */
    function Enter(opt) {
        if (this instanceof Enter) {
            this.opt = opt;
        } else { return new Enter(opt); }
    }
	Enter.prototype = new KeyQueue();
	Enter.prototype.constructor = Enter;
	Enter.prototype.test = function () {
		console.log("Enter");
	};
	

	/**
	 * Shift 键
	 * @param { Object } opt 选项信息
	 * @returns { Constructor } Scope safe constructor
	 */
	function Shift(opt) {
		if (this instanceof Shift) {
			this.opt = opt;
		} else { return new Shift(opt); }
	}
	Shift.prototype = new KeyQueue();
	Shift.prototype.constructor = Shift;
	Shift.prototype.test = function () {
		console.log("Shift");
	};
	
	
	/**
	 * Ctrl 键
	 * @param { Object } opt 选项信息
	 * @returns { Constructor } Scope safe constructor
	 */
	function Ctrl(opt) {
		if (this instanceof Ctrl) {
			this.opt = opt;
		} else { return new Ctrl(opt); }
	}
	Ctrl.prototype = new KeyQueue();
	Ctrl.prototype.constructor = Ctrl;
	Ctrl.prototype.test = function () {
		console.log("Ctrl");
	};


	/**
	 * Alt 键
	 * @param { Object } opt 选项信息
	 * @returns { Constructor } Scope safe constructor
	 */
	function Alt(opt) {
		if (this instanceof Alt) {
			this.opt = opt;
		} else { return new Alt(opt); }
	}
	Alt.prototype = new KeyQueue();
	Alt.prototype.constructor = Alt;
	Alt.prototype.test = function () {
		console.log("Alt");
	};
	

	/**
	 * CapsLock 键
	 * @param { Object } opt 选项信息
	 * @returns { Constructor } Scope safe constructor
	 */
	function CapsLock(opt) {
		if (this instanceof CapsLock) {
			this.opt = opt;
		} else { return new CapsLock(opt); }
	}
	CapsLock.prototype = new KeyQueue();
	CapsLock.prototype.constructor = CapsLock;
	CapsLock.prototype.test = function () {
		console.log("CapsLock");
	};

	
	/**
	 * End 键
	 * @param { Object } opt 选项信息
	 * @returns { Constructor } Scope safe constructor
	 */
	function End(opt) {
		if (this instanceof End) {
			this.opt = opt;
		} else { return new End(opt); }
	}
	End.prototype = new KeyQueue();
	End.prototype.constructor = End;
	End.prototype.test = function () {
		console.log("End");
	};
	

	/**
	 * Home 键
	 * @param { Object } opt 选项信息
	 * @returns { Constructor } Scope safe constructor
	 */
	function Home(opt) {
		if (this instanceof Home) {
			this.opt = opt;
		} else { return new Home(opt); }
	}
	Home.prototype = new KeyQueue();
	Home.prototype.constructor = Home;
	Home.prototype.test = function () {
		console.log("Home");
	};


	/**
	 * Left 键
	 * @param { Object } opt 选项信息
	 * @returns { Constructor } Scope safe constructor
	 */
	function Left(opt) {
		if (this instanceof Left) {
			this.opt = opt;
		} else { return new Left(opt); }
	}
	Left.prototype = new KeyQueue();
	Left.prototype.constructor = Left;
	Left.prototype.test = function () {
		console.log("Left");
	};


	/**
	 * Up 键
	 * @param { Object } opt 选项信息
	 * @returns { Constructor } Scope safe constructor
	 */
	function Up(opt) {
		if (this instanceof Up) {
			this.opt = opt;
		} else { return new Up(opt); }
	}
	Up.prototype = new KeyQueue();
	Up.prototype.constructor = Up;
	Up.prototype.test = function () {
		console.log("Up");
	};


	/**
	 * Right 键
	 * @param { Object } opt 选项信息
	 * @returns { Constructor } Scope safe constructor
	 */
	function Right(opt) {
		if (this instanceof Right) {
			this.opt = opt;
		} else { return new Right(opt); }
	}
	Right.prototype = new KeyQueue();
	Right.prototype.constructor = Right;
	Right.prototype.test = function () {
		console.log("Right");
	};


	/**
	 * Down 键
	 * @param { Object } opt 选项信息
	 * @returns { Constructor } Scope safe constructor
	 */
	function Down(opt) {
		if (this instanceof Down) {
			this.opt = opt;
		} else { return new Down(opt); }
	}
	Down.prototype = new KeyQueue();
	Down.prototype.constructor = Down;
	Down.prototype.test = function () {
		console.log("Down");
	};


	/**
	 * 无对应键盘码
	 * @param { Object } opt 选项信息
	 * @returns { Constructor } Scope safe constructor
	 */
	function nilCode(opt) {
		if (this instanceof nilCode) {
			this.opt = opt;
		} else { return new nilCode(opt); }
	}
	

	win.addEventListener("keydown", function (event) {
        var kEvent = new KeyClick(event.keyCode);
        var kHandler = kEvent.dispatch();
		kHandler.regist(kHandler.opt);
		kHandler.test();
    });
})();
