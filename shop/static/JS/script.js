;(function() {
'use strict';
window.onload = function() {




var show_menu = document.getElementById('show-menu');
var close_menu = document.getElementById('close-menu');
var menu = document.getElementById('menu');

var page_width = document.documentElement.clientWidth || document.documentElement.scrollWidth



if (page_width <= 1080) {
  show_menu.addEventListener('click', function (){menu.classList.add("slider-show");menu.classList.remove("slider-close");})
  close_menu.addEventListener('click', function() {menu.classList.add("slider-close");menu.classList.remove("slider-show");})	
}











};
})()
