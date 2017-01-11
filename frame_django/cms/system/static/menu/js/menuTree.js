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

var reload_ztree = function(){
    // $.ajax({
    //     async      : false,              //false，同步执行；默认true，异步执行，请求未完成就执行回调函数
    //     traditional: true,               //false，深度序列化参数对象；true，传统方式序列化参数对象
    //     cache      : false,
    //     type       : 'GET',
    //     dataType   : "json",
    //     data       : {},
    //     url        : "/menu/get_menu",                               //请求路径
    //     error: function () { alert('数据请求失败'); },                //请求失败处理函数
    //     success : function (data) { alert(data); treeNodes = data; } //请求成功处理函数，把后台封装好的简单Json赋给treeNodes
    //     complete: function (XMLHttpRequest, textStatus) {...}
    // });
    var node;
    var diy = "/static/common/css/zTreeStyle/img/diy/";
    for(i in menu_list){
        /**
         * 生成一个节点
         * 嵌套的三元运算符————条件1 ? 结果1: (条件2: ? 结果2: 结果3)
         * icon————节点自定义图标
         * iconOpen————父节点自定义展开时图标
         * iconClose————父节点自定义折叠时图标
         */
        node = {
            pId      : menu_list[i].parentid,
            id       : menu_list[i].id,
            name     : menu_list[i].menu_name+"(" + menu_list[i].code + ")",
            type     : menu_list[i].type,
            icon     : menu_list[i].type == 0 ? diy + "1_open.png" : (menu_list[i].type == 1 ? diy + "m1.png": diy + "3.png"),
            iconOpen : menu_list[i].type == 0 ? diy + "1_open.png" : (menu_list[i].type == 1 ? diy + "m1.png": diy + "3.png"),
            iconClose: menu_list[i].type == 0 ? diy + "1_close.png" : (menu_list[i].type == 1 ? diy + "m2.png": diy + "3.png")
        };
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
     * 添加、删除权限节点
     *
     * html页面文档加载时会对所有js/jq方法进行初始化
     * $(function() {})是在html文档加载中最后执行的
     * .suffixIcon是在$(function() {})中动态生成的html元素
     * on()函数如果放在$(function() {})外，文档初始化时将找不到.suffixIcon元素
     * 如果给html标签绑定onclick=fun(...)，fun()定义位置无限制
     *
     * $(selector).on(event[,childSelector[,data[,function[,map]]]])
     * event————一个或多个（有效的）事件或命名空间，由空格分隔多个事件值
     * childSelector————指定子元素触发事件，默认为null（此时相当于bind()函数）
     * data————传递到函数的额外数据
     * function————事件触发的函数（false也可以作为一个函数简写，返回false）
     * map————事件映射 ({event:function, event:function, ...})
     */
    $(".suffixIcon").on("click", function (e) {
        debugger;
        var target = e.target;
        var treeId = $(target).attr("data-treeId");
        var targetNode = zTree.getNodesByParam("id", treeId)[0];
        zTree.selectNode(targetNode);
        if ($(target).hasClass("add")) {
            menu[0].reset();
            $("#save_menu").attr("type", "add");
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
            var template = '<p>确定要删除【{{nodeName}}】吗?</p>';
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
 * @param treeId
 * @param treeNode
 */
function addDiyDom(treeId, treeNode) {
    /**
     * treeId————节点id
     * treeNode————节点对象
     */
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
        $("#menu").find("#parentid")       .val(md.parentid);
        $("#menu").find("#parentMenuName").text(md.parent_name ? md.parent_name + "(" + md.parent_url_code + ")" : '');
        $("#menu").find("#curId")          .val(md.id);
        $("#menu").find("#menuName")       .val(md.menu_name);
        $("#menu").find("#type")           .val(md.type).prop('disabled', true).css("cursor", "not-allowed");
        $("#menu").find("#urlCode")        .val(md.url_code);
        $("#menu").find("#code")           .val(md.code);
        $("#menu").find("#isvisible").prop("checked", md.isvisible == 1 ? true : false);
        $("#menu").find("#menuOrder")      .val(md.menu_order);
        $("#menu").find("#userNum").html("<a style='color:blue' href=\"/system/user.html?menuId="+treeNode.id+"\">" + md.user_num + "</a>");
        $("#menu").find("#roles")         .html(md.roles);
        $("#menu").find("#save_menu").attr("type", "edit");
    });
}


/**
 * 确认删除节点
 * @returns {boolean}
 */
function delNode() {
    /**
     * 获取zTree树对象
     */
    var zTree = $.fn.zTree.getZTreeObj("tree");
    var targetNode = zTree.getNodesByParam("id", $("#nodeId").val())[0];
    $.ajax({
        url: '/system/menu/delete',
        data: {"id": $("#nodeId").val()},
        type: 'post',
        dataType: "json",
        success: function (result) {
            $("#del_body").html(result.msg);
            $("#resultModal").modal('show');
            if (result.code == 0) {
                zTree.removeNode(targetNode);
            }
        }
    });
}


menu.validate({
    errorElement: 'span',
    errorClass: 'help-inline',
    focusInvalid: false,
    rules: {
        menu_name: {
            minlength: 2,
            required: true
        },
        url_code: {
            minlength: 1,
            required: true
        },
        menu_order: {
            integer: 0,
            required: true
        }
    },
    highlight: function (element) {
        $(element).closest('.help-inline').removeClass('ok');
        $(element).closest('.control-group').removeClass('success').addClass('error');
    },

    unhighlight: function (element) {
        $(element).closest('.control-group').removeClass('error');
    },
    success: function (label) {
        label.addClass('valid').addClass('help-inline ok')
            .closest('.control-group').removeClass('error').addClass('success');
    },
    submitHandler: function (form) {
        // TODO 验证通过执行的方法
    }
});