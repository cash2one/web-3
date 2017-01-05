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
     */
     callback: {
         //onRightClick : onRightClick,   //右键事件
        onClick: onClick,                 //节点被点击的事件
        // beforeDrop: beforeDrop,        //节点拖拽操作结束之前的事件
        // onDrop: onDrop                 //节点拖拽操作结束的事件
     },
    view: {
        addDiyDom: null,
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
    debugger;
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
     */
    $.fn.zTree.init($("#tree"), setting, treeNodes);
};

$(function() {
    reload_ztree();
});


/**
 * 点击节点
 * @param event
 * @param treeId
 * @param treeNode
 * @param clickFlag
 */
function onClick(event, treeId, treeNode, clickFlag) {
    document.getElementById("menu").reset();
    $.getJSON(base + '/system/menu/search', {"id": treeNode.id}, function (md) {
        $(menu).find("#parentid").val(md.parentid);
        $(menu).find("#parentMenuName").text(md.parentName ? md.parentName + "(" + md.parentUrlCode + ")" : '');
        $(menu).find("#curId").val(md.id);
        $(menu).find("#oldName").val(md.menuName);
        $(menu).find("#menuName").val(md.menuName);
        $(menu).find("#type").val(md.type).prop('disabled', true).css("cursor", "not-allowed");
        $(menu).find("#urlCode").val(md.urlCode);
        $(menu).find("#code").val(md.code);
        $(menu).find("#isOldSystem").val(md.isOldSystem);
        $(menu).find("#isOldSystem").prop("checked", md.isOldSystem == 1 ? true : false);
        $(menu).find("#isvisible").prop("checked", md.isvisible == 1 ? true : false);
        $(menu).find("#menuOrder").val(md.menuOrder);
        $(menu).find("#userNum").html("<a style='color:blue' href="+base+"/system/user.html?menuId="+treeNode.id+">" + md.userNum + "</a>");
        $(menu).find("#roles").html(md.roles);

        $("#save_menu").attr("type", "edit");
    });
}