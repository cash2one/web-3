/**
 * Created by ZDD on 2016/12/26.
 */

/**
 * setting————zTree的参数配置————JSON对象
 * 参考_setting
 */
var setting = {
    async: {
        enable: false,                                     //是否异步获取子节点数据，默认false
        contentType: "application/x-www-form-urlencoded",
        type: "post",
        dataType: "text",
        url: "",                                           //异步获取节点的URL地址，允许接收function的引用
        autoParam: [],                                     //异步加载时需要自动提交父节点属性的参数
        otherParam: [],                                    //提交的与节点数据相关的必需参数
        dataFilter: null                                   //数据过滤函数
    },
    /**
     * 回调函数
     * 默认参数————event, treeId, treeNode
     */
     callback: {
         //onRightClick : onRightClick,   //右键事件
        onClick: onClick,                 //节点被点击的事件
        // beforeDrop: beforeDrop,        //节点拖拽操作结束之前的事件
        // onDrop: onDrop                 //节点拖拽操作结束的事件
     },
    view: {
        addDiyDom: addDiyDom,            //在节点上固定显示用户自定义控件
        autoCancelSelected: true,
        dblClickExpand: true,
        expandSpeed: "fast",             //节点展开、折叠时的动画速度("slow", "normal", "fast"或毫秒数值，如：1000)
        fontCss: {color: 'blue'},        //个性化文字样式，默认{}
        nameIsHTML: false,
        selectedMulti: true,
        showIcon: true,                  //是否显示节点的图标
        showLine: true,                  //是否显示节点间的连线
        showTitle: true,
        txtSelectedEnable: false,
        checkable: true                  //每个节点上是否显示 CheckBox
    },
    data: {
        /**
         * 标准JSON数据————嵌套表示节点的父子包含关系
         * zTreeNodes = [{name: "***", children: [ {name: "***"}, ...]}]
         *
         * 简单JSON数据————使用id/pId表示节点的父子包含关系
         * zTreeNodes = [{"id":'***', "pId":'***', "name":"***"}, ...]
         */
        key: {
            children: "children",        //子节点键名
            name: "name",                //当前节点键名
            title: "",                   //节点提示信息属性名称
            url: "url",                  //节点链接的目标 URL 的属性名称
            icon: "icon"
        },
        simpleData: {
            enable: true,                //数据采用简单JSON格式，默认false
            idKey: "id",                 //当前节点唯一标识属性名
            pIdKey: "pId",               //当前节点父节点唯一标识属性名
            rootPId: null                //用于修正根节点父节点数据，即 pIdKey 指定的属性值
        }
    },
    check: {
        enable: false,                    //节点上是否显示 checkbox/radio
        autoCheckTrigger: false,
        chkStyle: 'checkbox',
        nocheckInherit: false,
        chkDisabledInherit: false,
        radioType: "level",
        chkboxType: {
            "Y": "ps",
            "N": "ps"
        }
    }
};

/**
 * zTreeNodes————zTree的全部节点数据集合————JSON数组
 */
var treeNodes = [];
var menu = $("#menu");
var diy = "/static/common/zTree/imgages/diy/";
var createNode = function (menu_obj) {
    return node = {
        pId      : menu_obj.parentid,
        id       : menu_obj.id,
        name     : menu_obj.menu_name+"(" + menu_obj.code + ")",
        type     : menu_obj.type,
        icon     : menu_obj.type == 0 ? diy + "1_open.png" : (menu_obj.type == 1 ? diy + "m1.png": diy + "3.png"),
        iconOpen : menu_obj.type == 0 ? diy + "1_open.png" : (menu_obj.type == 1 ? diy + "m1.png": diy + "3.png"),
        iconClose: menu_obj.type == 0 ? diy + "1_close.png" : (menu_obj.type == 1 ? diy + "m2.png": diy + "3.png")
    };
};


var reload_ztree = function(){
    // $.ajax({
    //     async      : false,                                    //默认true，异步执行（两个线程）；false，同步执行（请求期间锁住浏览器）
    //     traditional: true,                                     //false，深度序列化参数对象；true，传统方式序列化参数对象
    //     cache      : false,
    //     type       : 'GET',
    //     contentType："application/x-www-form-urlencoded",      //发送信息至服务器时内容编码类型
    //     dataType   : "json",                                   //服务器预期返回的数据类型（html、script、text、json、xml、jsonp）
    //     data       : {},
    //     url        : "/menu/get_menu",                         //请求路径
    //     error: function () { alert('数据请求失败'); },          //请求失败处理函数
    //     success : function (data) { treeNodes = data; }        //请求成功处理函数，把后台封装好的简单Json赋给treeNodes
    //     complete: function (XMLHttpRequest, textStatus) {...}
    // });
    var node;
    for(i in menu_list){
        /**
         * 生成一个节点
         * 嵌套的三元运算符————条件1 ? 结果1: (条件2: ? 结果2: 结果3)
         * icon————节点自定义图标
         * iconOpen————父节点自定义展开时图标
         * iconClose————父节点自定义折叠时图标
         */
        node = createNode(menu_list[i]);
        treeNodes.push(node);
    }
    /**
     * $.fn.zTree.init(jQueryObj, setting, treeNodes)————v3.0
     * jQueryObj.zTree(setting, zTreeNodes)————v2.6
     * .expandAll(true)————可选函数，是否展开全部节点（默认false）
     */
    $.fn.zTree.init($("#tree"), setting, treeNodes).expandAll(true);
};


$(function() {
    reload_ztree();
    var zTree = $.fn.zTree.getZTreeObj("tree");
    /**
     * 添加、删除节点
     *
     * html页面文档加载时会对所有js/jq方法进行初始化
     * $(document).ready(function(){})————$(function(){})————window.onload=function(){}————<body onload="XXX">————在html文档加载中最后执行
     * .suffixIcon是在$(function(){})中动态生成的html元素
     * on()函数如果放在$(function(){})外，文档初始化时将找不到.suffixIcon元素
     *
     * 如果给html标签绑定onclick=fun(...)，fun()定义位置无限制
     * 浏览器console是实时的，与文档加载无关
     *
     * $(selector).on(event[,childSelector[,data[,function[,map]]]])
     * event————一个或多个（有效的）事件或命名空间，由空格分隔多个事件值
     * childSelector————指定子元素触发事件，默认为null（此时相当于bind()函数）
     * data————传递到函数的额外数据
     * function————事件触发的函数（false也可以作为一个函数简写，返回false）
     * map————事件映射 ({event:function, event:function, ...})
     */
    $(".suffixIcon").on("click", function (e) {
        var target = e.target;
        var treeId = $(target).attr("data-treeId");
        var targetNode = zTree.getNodesByParam("id", treeId)[0];
        zTree.selectNode(targetNode);
        if ($(target).hasClass("add")) {
            menu[0].reset();
            $("#save_menu").attr("change_type", "add");
            $.getJSON("/system/menu/get_menu", {"id": treeId}, function (menu) {
                $("#menu").find("#parentMenuName").text(menu.menu_name + "(" + menu.url_code + ")");
                $("#menu").find("#parentid").val(menu.id);
                if (menu.type == 0) {
                    $("#menu").find("#type").removeAttr("disabled").css("cursor", "default");
                    $("#menu").find("#type option").eq(2).prop('disabled', true).siblings().removeAttr('disabled');
                } else if (menu.type == 1) {
                    $("#menu").find("#type").removeAttr("disabled").css("cursor", "default").val(2);
                    $("#menu").find("#type option").eq(2).removeAttr('disabled').siblings().prop('disabled', true);
                }
            })
        } else if ($(target).hasClass("del")) {
            var data = {nodeName: targetNode.name};
            //var template = '<p>确定要删除【{{nodeName}}】吗?</p>';
            var template = $("#ptemplate").html();
            var view = Mustache.render(template, data);
            $("#del_body").html(view);
            $("#nodeId").val(targetNode.id);
            $("#delModel").modal('show');
        }
        /**
         * 阻止点击事件向上冒泡————.suffixIcon在节点li内，点击时会触发onClick函数
         */
        e.stopPropagation();
    });
});



var IDMark_A = "_a";
/**
 * 添加编辑图标
 * @param treeId————节点id
 * @param treeNode————节点对象
 */
function addDiyDom(treeId, treeNode) {
    var aObj = $("#" + treeNode.tId + IDMark_A);
    if (treeNode.id != 1) {
        var delStr = "<span class='suffixIcon' title='删除[" + treeNode.name + "]' onfocus='this.blur();'><span class='button del' data-treeId='" + treeNode.id + "'></span></span>";
        aObj.append(delStr);
    }
    // 权限
    if (treeNode.type < 2) {
        var addStr = "<span class='suffixIcon' title='新增子[" + (treeNode.type == 0 ? "目录/菜单" : "操作") + "]' onfocus='this.blur();'><span class='button add' data-treeId='" + treeNode.id + "'></span></span>";
        aObj.append(addStr);
    }
}


/**
 * 编辑权限节点
 * 参数见API文档————http://www.treejs.cn/v3/api.php
 */
function onClick(event, treeId, treeNode, clickFlag) {
    document.getElementById("menu").reset();
    $.getJSON('/system/menu/get_menu', {"id": treeNode.id}, function (md) {
        menu.find("#parentid")       .val(md.parentid);
        menu.find("#parentMenuName").text(md.parent_name ? md.parent_name + "(" + md.parent_url_code + ")" : '');
        menu.find("#curId")          .val(md.id);
        menu.find("#oldName")        .val(md.menu_name);
        menu.find("#menuName")       .val(md.menu_name);
        menu.find("#type")           .val(md.type).prop('disabled', true).css("cursor", "not-allowed");
        menu.find("#urlCode")        .val(md.url_code);
        menu.find("#code")           .val(md.code);
        menu.find("#isvisible").prop("checked", md.isvisible == 1 ? true : false);
        menu.find("#menuOrder")      .val(md.menu_order);
        menu.find("#userNum").html("<a style='color:blue' href=\"/system/user.html?menuId="+treeNode.id+"\">" + md.user_num + "</a>");
        menu.find("#roles")         .html(md.roles);
        menu.find("#save_menu").attr("type", "edit");
    });
}


/**
 * 确认删除节点
 * @returns {boolean}
 */
function delNode() {
    var zTree = $.fn.zTree.getZTreeObj("tree");
    var targetNode = zTree.getNodesByParam("id", $("#nodeId").val())[0];
    debugger;
    $.ajax({
        url: '/system/menu/delete_menu',
        data: {
            "id": $("#nodeId").val(),
            csrfmiddlewaretoken: getCookie('csrftoken'),
            // csrfmiddlewaretoken: '{{ csrf_token }}',
        },
        type: 'post',
        dataType: "json",
        success: function (result) {
            $("#result_body").html(result.msg);
            $("#resultModal").modal('show');
            if (result.code == 0) {
                zTree.removeNode(targetNode);
            }
        }
    });
}

/**
 * 使用easyform————表单验证插件————http://thesmallcar.github.io/jQuery.easyform/
 */
$(document).ready(
    function(){
        var ef = menu.easyform();
        // ef.is_submit = false;
        ef.success = function(ef){
            save(ef);
        }
    });


/**
 * 保存
 * 添加或修改
 */
function save(ef) {
    var type = $("#save_menu").attr("change_type");
    if (type == "add") {
        $("#curId").val('');
    }

    if (type != 'add') {
        var curId = $("#curId").val();
        if (curId == 1) {
            alert("不允许修改根节点");
            return false;
        }
    }

    var data = {
        menuName: $('#menuName').val(),
        oldName: $('#oldName').val()
    };
    var template = '<p>确定要' + (type == 'add' ? '新增权限【{{menuName}}' : '修改权限【{{oldName}}') + '】吗？</p>';
    var view = Mustache.render(template, data);
    $("#add_body").html(view);
    $("#addModal").modal('show');
    ef.is_submit = false;
}

function addNode() {
    /**
     * 获取zTree树对象
     */
    var zTree = $.fn.zTree.getZTreeObj("tree");
    var type = $("#save_menu").attr("change_type");
    /**
     * serialize()————jq序列化表单值
     */
    $.ajax({
        url: '/system/menu/save_menu',
        type: 'post',
        data: $(menu).serialize(),
        dataType: "json",
        success: function (result) {
            $("#ret_body").html(result['msg']);
            $("#retModal").modal('show');
            if (result.code == 0) {
                // 新增-异步添加节点，修改-刷新节点
                var menu_obj = result['menu_obj'];

                if (type == "add") {
                    var parentNode = zTree.getNodesByParam("id", $("#parentid").val(), null);
                    var newNode = createNode(menu_obj);
                    zTree.addNodes(parentNode[0], newNode);
                } else {
                    var targetNode = zTree.getNodesByParam("id", menu_obj.id, null)[0];
                    targetNode.name = menu_obj.menu_name;
                    zTree.updateNode(targetNode);
                }
            }
        }
   });
}


/**
 * js获取csrf_token，用于ajax提交数据
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