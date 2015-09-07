/**
 * @fileOverview Homepage controls
 * @name homepage.js
 * @author Young Lee youngleemails@gmail.com
 * @license MIT
 */
define(function (homepage) {
    var model = {},
        view = {
            render: function () {
                $('#homepage-txt').fadeOut('slow');
            }
        };

    _.extend(model, Backbone.Events);
    _.extend(view, Backbone.Events);

    model.on({
        "homepage:info": function (msg) {
            console.log("Young Lee " + msg);
        }
    });
    model.once({
        "younglee:rss": function (msg) {
            console.log("Young Lee " + msg);
        }
    });

    $('body').on('keypress', function () {
        model.trigger("homepage:info", "keybind");
    });
    $("#rss-icon").click(function () {
        model.trigger("homepage:rss", "rss");
        model.off("homepage:rss");
    });
    view.listenTo(model, "homepage:info", view.render);
});
