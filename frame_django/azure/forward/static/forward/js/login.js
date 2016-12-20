/**
 * Created by ZDD on 2016/12/19.
 */
var getcode = function(){
    $.ajax({
        url: '/forward/getcode',
        data: {email: $("[name=email]").val()},
        success: function(data) {
            alert(data)
        }
    })
};