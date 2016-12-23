/**
 * Created by Administrator on 2016/7/17.
 */
var getEmailCode = function() {
    $.ajax({
        url: '/login/get_email_code',
        data: {email: $("[name=email]").val()},
        success: function(data) {
            alert(data)
        }
    })
};


$(function() {
    $('[name=tip]').tipso({
        //position: 'top',
        //speed: 400,
        //delay: 200,
        //width: 200,
        //color: '#ffffff',
        useTitle: false,
        offsetX: 60,
        background: 'tomato'
    });
    $('#tip_security_code').tipso({
        useTitle: false,
        offsetX: 100,
        background: 'tomato'
    });
    $("#email_register").validate({
        //debug: true,
        rules: {
            email: {
                required: true,
                email: true
            },
            security_code: {
                required: true,
                rangelength:[4, 5]
            },
            pwd: {
                required: true,
                password: true,
                rangelength:[6, 13]
            },
            pwd2: {
                required: true,
                equalTo: "#pwd"
            }
        },
        messages: {
            email: {
                required: "请填写邮箱地址",
                email: "邮箱格式不正确"
            },
            security_code: {
                required: "请填写验证码",
                rangelength: "验证码长度不正确"
            },
            pwd: {
                required: "请填写密码",
                rangelength: "密码长度不正确"
            },
            pwd2: {
                required: "请填写密码",
                equalTo: "两次输入密码不匹配"
            }
        },
        errorPlacement: function(error, element){
            element.parent().attr("data-tipso", error.html());
        }
    });
});
