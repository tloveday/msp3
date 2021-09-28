$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.social-media').hover(
        function(){ $(this).toggleClass('pulse') });
    $('input#headline, textarea#review').characterCounter();
})


//Guide for making the Star Rating System in JQuery from Happy Coder on Youtube - https://www.youtube.com/watch?v=1xW6DPpwcDM&t=14s
var a;
var clicked;


$('.rating-star').click(function(){
    $('.rating-star').removeClass('rating-hover rating-picked');
    
    $(this).removeClass('far').addClass('rating-picked fas');
    $(this).prevAll().addClass('rating-picked fas');
    $(this).nextAll().addClass('fas')

})