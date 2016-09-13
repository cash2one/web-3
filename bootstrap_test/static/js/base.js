$("#nav-ul li").mouseover(function () {
    $(this).addClass("active");
})
$("#nav-ul li").mouseleave(function () {
    $(this).removeClass("active");
})


var returnTop = $('#returnTop');
window.onscroll = function(){
    var top = document.documentElement.scrollTop || document.body.scrollTop;
    if(top > 0){
        returnTop.css('display', 'block');
    }
    else{
        returnTop.css('display', 'none');  
    }
}

returnTop.hover(function () {
    returnTop.toggleClass('bg-primary');
    returnTop.toggleClass('bg-default');
})

returnTop.click(function(){
    // $(document).scrollTop(0);
    document.documentElement.scrollTop = document.body.scrollTop =  0;
})


$("#page-brake li").hover(function () {
    $(this).toggleClass("active");
})
