/**
 * @fileOverview Page Class
 * @name page.js
 * @author Young Lee youngleemails@gmail.com
 * @license MIT
 */
function Page(type) {
    if (this instanceof Page) {
        this.type = type;
    } else {
        return new Page(type);
    }
}

Page.prototype = {
    constructor: Page,
    getPageType: function () {
        return this.type;
    }
};
