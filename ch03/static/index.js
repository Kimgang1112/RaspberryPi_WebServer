const off=document.getElementById('off');
const on=document.getElementById('on');

const off_button=document.getElementById('off_button');
const on_button=document.getElementById('on_button');

on_button.addEventListener("click", function() {
    location.href='/on';

})

off_button.addEventListener("click", function() {
    location.href='/off';

})