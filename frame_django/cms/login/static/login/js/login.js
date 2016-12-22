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
