 $(document).ready(function(){
    $(window).scroll(function(){
         var scroll= $(window).scrollTop();
            if (scroll>0){
                 $(nav).css("background","#000");
                 $("nav a").css('color','white');
             }
            else{
                 $(nav).css("background","transparent");
                 $("nav a").css('color','black');
             }
     })
 })