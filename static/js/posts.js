/////////////////////////////
// JavaScript for Posts page
////////////////////////////

$(function() {
    // Executed when js-menu-icon clicked
    $('.js-menu-icon').click(function() {
        // $(this) : self element, namely div.js-menu-icon
        // next() : Next to div.js-menu-icon, div.menu
        // toggle() : Switch Show and hide
        $(this).next().toggle();
    })
})