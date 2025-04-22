$(document).ready(function(){
   
     
eel.expose(DisplayMessage)
function DisplayMessage(message){
    $(".siri-message li:first").text(message);
    $('.siri-message').textillate('start');

}

eel.expose(ShowHood)
function ShowHood(){
    $("#Oval").attr("hidden", false);
    $("#Siriwave").attr("hidden", true);

}

});

