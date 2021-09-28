$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.social-media').hover(
        function(){ $(this).toggleClass('pulse') });
    $('input#headline, textarea#review').characterCounter();
})


//Guide for making the Star Rating System in JQuery from Happy Coder on Youtube - https://www.youtube.com/watch?v=1xW6DPpwcDM&t=14s
