"use strict";

// Unit Test
function assert(value, desc) {
	var li = document.createElement("li");
	li.className = value ? "pass" : "fail";
	li.appendChild(document.createTextNode(desc));    // add Text
	document.getElementById("results").appendChild(li);
}

window.onload = function () {
	assert(true, "the test suite is running");
	assert(false, "Fails!");
};
