/**
 * 顶部导航栏
 */
$("#nav-ul li").mouseover(function () {
    $(this).addClass("active");
});
$("#nav-ul li").mouseleave(function () {
    $(this).removeClass("active");
});


/**
 * 侧边栏
 */





/**
 * 返回頂部
 */
var returnTop = $('#returnTop');
window.onscroll = function(){
    var top = document.documentElement.scrollTop || document.body.scrollTop;
    if(top > 0){
        returnTop.css('display', 'block');
    }
    else{
        returnTop.css('display', 'none');
    }
};
returnTop.hover(function () {
    returnTop.toggleClass('bg-primary');
    returnTop.toggleClass('bg-default');
});
returnTop.click(function(){
    // $(document).scrollTop(0);
    document.documentElement.scrollTop = document.body.scrollTop =  0;
});


/**
 * 底部导航栏
 */
$(document).ready(function(){
    //alert($(document.body).height());
    //alert($(window).height());
    //if($(document.body).height() < $(window).height()){
        //$("#nav-bottom").removeClass("navbar-static-bottom");
        //$("#nav-bottom").addClass("navbar-fixed-bottom");
    //}
});
