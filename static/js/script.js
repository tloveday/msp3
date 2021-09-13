$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.social-media').hover(
        function(){ $(this).toggleClass('pulse') });
})