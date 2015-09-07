/**
 * @fileOverview Page Time Display
 * @name time.js
 * @author YoungLee youngleemails@gmail.com
 * @license MIT
 */
define(function (time) {
    $('#minibuffer .time').pseudoheartbeat(1000, function () {
        // Construct
        var timer = new Date(),
            date = timer.toLocaleDateString(),
            time = timer.getHours() + ":" + timer.getMinutes() + ":" + timer.getSeconds();

        $(this).text(timer.toLocaleString());

        // Deconstruct
        timer = null;
    });
});
