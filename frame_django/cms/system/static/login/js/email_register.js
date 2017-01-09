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
        // url: "{% url 'url_name' %}",   //只能写在html文件里
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

/**
 * submit提交————type=submit默认绑定onclick(form.submit())
 * method:get/post————默认get
 * action:url————默认当前页面地址（不写action或action=""）,get不能用url传值
 * action="./?"————./代表当前目录，?代表查询字符串为空
 * action="?" ————提交给自己
 * 表单中每一个input标签都需要有一个name属性
 */

/**
 * submitForm({ url:***, dataType:"text", callback:function(data){***} })
 */

/**
 * ajax提交————用于实现异步请求局部刷新（可以在回调函数里跳转/刷新页面）
 * $.get(URL[,data[,function(data,status,xhr)[,dataType]]])
 * 后台无需在视图函数中定义参数
 *
 * load( url[,data[,function(response,status,xhr)]] )————一种简单强大的AJAX 函数
 * response————包含来自请求的结果数据
 * status————包含请求的状态（"success"、"notmodified"、"error"、"timeout"、"parsererror"）
 * xhr————包含 XMLHttpRequest 对象
 * 自动给调用load的对象填充
 */

//
// onclick中使用当前对象需要传递$(this)参数


$(function()
{
    tipsoInit();
    /**
     * 使用validate.js验证表单
     */
    $("#email_register").validate(
        //debug: true,
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
                //error：错误消息元素
                //element：验证元素
                //error.appendTo(element.parent().parent().next());
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
