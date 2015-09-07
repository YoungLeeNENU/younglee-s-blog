/**
 * @fileOverview cursor control
 * @name cursor.js
 * @author Young Lee <youngleemails@gmail.com>
 * @license MIT
 */
define(function (cursor) {
    // Dot blink for homepage
    (function () {
        var blink = 0;
        $.heartbeat(500, function () {
            if (blink % 2 === 0) {
                $('#blink-cursor').hide();
                $('#yl-dot').css({ color: "#161A1F" });
            } else {
                $('#blink-cursor').show();
                $('#yl-dot').css({ color: "#ee4000" });
            }
            blink += 1;
            blink %= 2;
        });
    })();
});
