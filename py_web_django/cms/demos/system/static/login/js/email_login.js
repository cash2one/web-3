/**
 * Created by zdd on 2016/12/25.
 */
var tipsoInit = function() {
    $('[name=tip]').tipso({
        //speed           : 400,        //动画持续时间
        //color           : '#ffffff',  //文本颜色
        //postiion        : 'top',      //显示位置
        //width           : 200,        //宽度
        //delay           : 200,        //延迟
        //offsetX         : 0,          //水平偏移
        //offsetY         : 0,          //垂直偏移
        //content         : null,       //内容
        //ajaxContentUrl  : null,       //异步加载内容
        //useTitle        : true,       //使用 title 属性值作为内容
        //onBeforeShow    : null,       //执行前的回调函数
        //onShow          : null,       //显示前的回调函数
        //onHide          : null,       //显示后的回调函数
        useTitle: false,
        offsetX: 60,
        background: 'tomato',
        onBeforeShow: function() {
            if($(this)[0].content=="ok") {
                $(this)[0].stopShow = true;
            } else {
                $(this)[0].stopShow = false;
            }
        }
    });
};


$(function() {
    tipsoInit();
    $("#email_login").validate({
        rules: {
            email: {
                required: true,
                email: true
            },
            pwd: {
                required: true,
                password: true,
                rangelength:[6, 13]
            }
        },
        messages: {
            email: {
                required: "请填写邮箱地址",
                email: "邮箱格式不正确"
            },
            pwd: {
                required: "请填写密码",
                rangelength: "密码长度不正确"
            }
        },
        errorPlacement: function(error, element){
            element.parent().attr("data-tipso", error.html());
            if(error.html().length != 0){
                element.parent().tipso('update', 'content', error.html());
                element.parent().tipso('show');
            } else {
                element.parent().tipso('update', 'content', "ok");
                element.parent().tipso('hide');
            }
        },
        success: 'valid'
    });
    $("[name=tip]").validate({
        onsubmit: true,
        onfocusout: true,
        focusInvalid: true
    })
});