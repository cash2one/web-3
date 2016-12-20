/**
 * Created by ZDD on 2016/12/8.
 */

/**
 * ajax提交数据中添加csrf_token
  * @param name
 * @returns {*}
 */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
//jQuery Cookie插件————基于jquery，可以对cookie做读、写、删等操作
//var csrftoken = $.cookie('csrftoken');

var addDownload = function() {
    $.ajax({
        url: "/download_list/add_download",
        type: 'post',
        //dataType: "html",
        data: {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            create_name: $("[name=create_name]").val(),
            file_name: $("[name=file_name]").val(),
            address: $("[name=address]").val()
        },
        success: function(data) {
            if(data=="ok"){
                alert("添加成功");
                window.location.reload();
            } else {
                alert(data);
            }
        }
    })
};


var reportExcel = function() {
    $("#download_form").attr('action','/download_list/report_excel');
    $("#download_form").submit();
    $("#download_form").attr('action','');
};


var clearForm = function() {
    $("#download_form")[0].reset();
    window.location.href = "/download_list";
};