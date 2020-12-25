$(document).ready(function(){
    // THis is the maximum number of add more button can create child
    var maxGroup = 10;
    
    //add more main-container uses this function
    $(".add_field_button").click(function(){
        if($('body').find('.original').length < maxGroup){
            var fieldHTML = '<div class="main-container original">'+$(".originalCopy").html()+'</div>';
            $('body').find('.original:last').after(fieldHTML);
        }else{
            alert('Maximum '+maxGroup+' groups are allowed.');
        }
    });
    
    //The copy of the class at the bottom can be removed using the remove button
    $("body").on("click",".remove",function(){ 
        $(this).parents(".original").remove();
    });
});