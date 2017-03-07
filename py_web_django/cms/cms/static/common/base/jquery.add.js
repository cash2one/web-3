/**
 * Created by ZDD on 2016/12/5.
 */

/**
 * validate自定义validate表单验证规则
 */
$.validator.addMethod(
    "phone",
    function (value, element) {
        var pattern  = /^1\d{10}$/;
        return this.optional(element) || (pattern.test(value));
    },
    "手机号格式不正确"
);
$.validator.addMethod(
    "password",
    function (value, element) {
        var pattern  = /^[a-zA-Z0-9_@%-]{6,12}$/;
        return this.optional(element) || (pattern.test(value));
    },
    "密码格式不正确"
);


/**
 * validator自定义提示信息(覆盖默认的)参照messages_zh.js
 */
//$.extend($.validator.messages, {
//    required: "必选字段",
//});

