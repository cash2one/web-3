/**
 * Created by Administrator on 2016/7/17.
 */

// submit提交
// method:get/post————默认get
// action:url————get不能用url传值，默认当前页面地址（不写action或action=""）
// action="./?"————./代表当前目录，?代表查询字符串为空
// action="?" ————提交给自己
// 表单中每一个input标签都需要有一个name属性
// type=submit默认绑定onclick(form.submit())
//
// submitForm({ url:***, dataType:"text", callback:function(data){***} })
//
// ajax提交————用于实现异步请求局部刷新
// 本身不会跳转页面、不改变地址栏、不刷新页面（可以在回调函数里跳转）
// $.get(URL[,data[,function(data,status,xhr)[,dataType]]])
// 适用于在回调函数中获取后台返回的值，然后据此操作html属性方法，局部更新页面
// 后台无需在视图函数中定义参数
//
// load( url[,data[,function(response,status,xhr)]] )————一种简单强大的AJAX 函数
// response————包含来自请求的结果数据
// status————包含请求的状态（"success"、"notmodified"、"error"、"timeout"、"parsererror"）
// xhr————包含 XMLHttpRequest 对象
// 自动给调用load的对象填充
//
// onclick中使用当前对象需要传递$(this)参数


$(function() {
    // 使用validate.js验证表单
    $("#register_form").validate({
        //debug: true,
        rules: {
            phone: {
                required: true,
                phone: true
            },
            passwd: {
                required: true,
                passwd: true
            },
            passwd1: {
                required: true,
                equalTo: "#passwd"
            }
        },
        messages: {
            phone: {
                required: "电话号码必填"
            },
            passwd: {
                required: "密码必填"
            },
            passwd1: {
                required: "必填字段",
                equalTo: "两次输入密码不一致"
            }
        },
        // 错误信息提示位置
        errorPlacement: function(error, element){
            // error：错误消息元素
            // element：验证元素
            //error.appendTo(element.parent());
            //error.appendTo(element.parent().parent());
            error.appendTo(element.parent().next());
        }
    });
    $("#login_form").validate({
        //debug: true,
        rules: {
            phone: {
                required: true,
                phone: true
            },
            passwd: {
                required: true,
                passwd: true
            }
        },
        messages: {
            phone: {
                required: "电话号码必填"
            },
            passwd: {
                required: "密码必填"
            }
        },
        errorPlacement: function(error, element){
            error.appendTo(element.parent().next());
        }
    })
});
