/**
 * Created by Administrator on 2016/7/17.
 */
var wait=60;
/**
 * 倒计时函数[js/jq混合写法]
 * @param e
 */
function time(e)
{
    if (wait == 0)
    {
        //e.removeAttribute("disabled");
        //e.value="获取验证码";
        $(e).attr("onclick","getEmailCode($(this));");
        $(e).css("cursor", "pointer");
        e.innerHTML = "获取验证码";
        wait = 60;
    }
    else
    {
        //e.setAttribute("disabled", true);
        //e.value="重新发送(" + wait + ")";
        $(e).removeAttr("onclick");
        $(e).css("cursor", "wait");
        e.innerHTML="重新发送(" + wait + ")";
        wait--;
        setTimeout(function()
        {
            time(e)
        },
            1000
        )
    }
}

var getEmailCode = function(e) {
    $.ajax({
        url: '/login/get_email_code',
        data: {email: $("[name=email]").val()},
        success: function(data) {
            if(data=="ok")
            {
                alert("验证码已发送，请在10分钟内完成注册");
                time(e[0]);
            }
            else
            {
                alert(data);
            }
        }
    });
};

var tipsoInit = function() {
    $('[name=tip], #tip_security_code').tipso({
        useTitle: false,
        offsetX: 60,
        background: 'tomato',
        onBeforeShow: function() {
            if($(this)[0].content=="ok") {
                //$(this)[0].background = "#55b555";
                $(this)[0].stopShow = true;
            } else {
                $(this)[0].stopShow = false;
            }
        }
    });
    $('#tip_security_code').tipso('update', 'offsetX', 100)
};


$(function()
{
    tipsoInit();
    $("#email_register").validate(
        {
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
                if(error.html().length != 0){
                    element.parent().tipso('update', 'content', error.html());
                    element.parent().tipso('show');
                } else {
                    element.parent().tipso('update', 'content', "ok");
                    element.parent().tipso('hide');
                }
            },
            success: 'valid'
        }
    );
    $("[name=tip], #tip_security_code").validate(
        {
            onsubmit: true,
            onfocusout: true,
            focusInvalid: true
        }
    )
});
