$(document).ready(function(){
    $(".fa-bars").click(function(){
        $(".menu").animate({left:"270px"}, 600);
        $(".menu").css("visibility", "visible");
        $(".fa-bars").animate({left:"270px"}, 600);
        $(".text_1").animate({left:"770px"}, 600);
        $(".fa-close").css("visibility", "visible");
        $(".fa-close").animate({left:"270px"}, 600);
        $(".fa-bars").css("visibility", "hidden");
    });
});

$(document).ready(function(){
    $(".fa-close").click(function(){
        $(".menu").animate({left:"270px"}, 700);
        $(".menu").css("visibility", "hidden");
        $(".fa-bars").animate({left:"0px"}, 600);
        $(".text_1").animate({left:"685px"}, 600);
        $(".fa-close").css("visibility", "hidden");
        $(".fa-close").animate({left:"0px"}, 600);
        $(".fa-bars").css("visibility", "visible");
    });
});