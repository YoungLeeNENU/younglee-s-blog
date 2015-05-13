/**
 * @fileOverview Homepage controls
 * @name homepage.js
 * @author Young Lee youngleemails@gmail.com
 * @license MIT
 */
$(document).ready(function () {
	var model = {},
		view = {
			render: function () {
				$('#homepage-txt').fadeOut('slow');
			}
		};

	_.extend(model, Backbone.Events);
	_.extend(view, Backbone.Events);

	model.on({
		"younglee:info": function (msg) {
			console.log("Young Lee " + msg);
		}
	});
	model.once({
		"younglee:rss": function (msg) {
			console.log("Young Lee " + msg);
		}		
	});

	$("#hotkey-icon").click(function () {
		model.trigger("younglee:info", "keybind");
	});
	$("#rss-icon").click(function () {
		model.trigger("younglee:rss", "rss");
		model.off("younglee:rss");
	});
	view.listenTo(model, "younglee:info", view.render);
});
