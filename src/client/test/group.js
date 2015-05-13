"use strict";

(function (context) {
	var results;

	context.assert = function (value, desc) {
		var li = document.createElement("li");
		li.className = value ? "pass" : "fail";
		li.appendChild(document.createTextNode(desc));
		results.appendChild(li);
		if (!value) {    // 每组中一个失败代表整组测试的失败
			li.parentNode.parentNode.className = "fail";
		}
		return li;    // return a DOM element
	};

	context.test = function (name, fn) {
		results = document.getElementById("results");
		results = context.assert(true, name).appendChild(document.createElement("ul"));
		fn();
	};
})(this);

window.onload = function () {
	test("Test A.", function () {
		assert(true, "First assertion completed");
		assert(true, "Second assertion completed");
		assert(true, "Third assertion completed");
	});
	test("Test B", function () {
		assert(true, "First test completed");
		assert(false, "Second test failed");
		assert(true, "Third test completed");
	});
	test("Test C", function () {
		assert(null, "fail");
		assert(5, "pass");
	});
};
