$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.social-media').hover(
        function(){ $(this).toggleClass('pulse'); });
    $('.datepicker').datepicker();
    $('input#headline, textarea#review').characterCounter();
    $('.modal').modal();
});


//Guide for making the Star Rating System in JQuery from Happy Coder on Youtube - https://www.youtube.com/watch?v=1xW6DPpwcDM&t=14s edited to meet design
var a;
var clicked;


$('.rating-star').click(function(){
    rating = $('i.rating-hover').length;
    $('.rating-star').removeClass('rating-hover rating-picked');
    $(this).removeClass('far').addClass('rating-picked fas');
    $(this).prevAll().addClass('rating-picked fas');
    $(this).nextAll().addClass('far');

    a = $(this).index();


    clicked == $($('.rating-star').get(a));

    $(clicked).data('clicked', true);
    $('#review_counter').val(rating);
    console.log('rated ' + rating);

});

$('.rating-star').hover(function(){
    $('.rating-star').removeClass('rating-hover rating-picked');
    
    $(this).addClass('rating-hover');
    $(this).prevAll().addClass('rating-hover');

});

$('rating-star').mouseout(function(){
    $('.rating-star').removeClass('rating-hover');

    if ($(clicked).data('clicked')){
        $(clicked).addClass('rating-picked');
        $(clicked).prevAll().addClass('rating.chosen');
    }
});