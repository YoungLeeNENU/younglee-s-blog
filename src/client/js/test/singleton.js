var context = this;

var singleTon = function () {
	var ins = new Array();

	context.setIns = function (item) {
		ins.push(item);
	};

	context.getIns = function (index) {
		console.log(ins);
	};
	
	return ins || new Array();
}();
