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
         //onRightClick : onRightClick   //右键事件
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
         * 标准的JSON数据————嵌套表示节点的父子包含关系
         * 简单的JSON数据————使用id/pId表示节点的父子包含关系
         */
        simpleData: {
            enable: true,                //数据是否采用简单Array格式，默认false
            idKey: "id",                 //当前节点唯一标识的属性名称
            pIdKey: "pId",               //当前节点的父节点唯一标识的属性名称
            rootPId: null                //用于修正根节点父节点数据，即 pIdKey 指定的属性值
        },
        key: {
            children: "children",        //子节点名称
            name: "name",                //当前节点名称
            title: "",                   //节点提示信息属性名称
            url: "url",                  //节点链接的目标 URL 的属性名称
            icon: "icon"
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
 * $.fn.zTree.init(jQueryObj, setting, treeNodes)————v3.0
 * jQueryObj.zTree(setting, zTreeNodes)————v2.6
 */
var treeNodes = [];

treeNodes = [
    {"id":1, "pId":0, "name":"test1"},
    {"id":11, "pId":1, "name":"test11"},
    {"id":12, "pId":1, "name":"test12"},
    {"id":111, "pId":11, "name":"test111"}
];

var reload_ztree = function(){
    /*
    $.ajax({
        async      : false,
        traditional: true,              //false，深度序列化参数对象
        cache      : false,
        type       : 'GET',
        dataType   : "json",
        data       : {},
        url        : "/menu/get_menu",   //请求路径
        error: function () {       //请求失败处理函数
            alert('数据请求失败');
        },
        success : function (data) {    //请求成功处理函数
            alert(data);
            treeNodes = data;         //把后台封装好的简单Json格式赋给treeNodes
        }
    });
    */
    $.fn.zTree.init($("#tree"), setting, treeNodes);
};

$(function() {
    reload_ztree();
});