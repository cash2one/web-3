/**
 * Created by ZDD on 2016/12/26.
 */

/**
 * setting————zTree的参数配置————JSON对象
 */
var setting = {
    // async             : true,    //是否异步获取子节点数据，默认false
    // asyncUrl          : url,     //async = true 时，设置异步获取节点的URL地址，允许接收function的引用
    // asyncParam        : ["id"],  //提交的与节点数据相关的必需参数
    isSimpleData      : true,       //数据是否采用简单Array格式，默认false
    treeNodeKey       : "id",       //在isSimpleData格式下，当前节点键名称
    treeNodeParentKey : "pId",      //在isSimpleData格式下，当前节点的父节点键名称
    // nameCol : "currentNode",     //在isSimpleData格式下，当前节点名称
    showLine          : true,       //是否显示节点间的连线
    // checkable         : true,    //每个节点上是否显示 CheckBox
    expandSpeed       : "fast",     //zTree节点展开、折叠时的动画速度("slow", "normal", "fast"或毫秒数值，如：1000)
    /**
     * 回调函数
     */
    // callback: {
    //     rightClick : zTreeOnRightClick     //右键事件
    // },

    data: {
        simpleData: {
            enable: true
        }
    }
};

/**
 * zTreeNodes————zTree的全部节点数据集合————JSON数组
 * zTree(setting, [zTreeNodes])
 */
var treeNodes;
var zTree;

treeNodes = [
    {"id":1, "pId":0, "name":"test1"},
    {"id":11, "pId":1, "name":"test11"},
    {"id":12, "pId":1, "name":"test12"},
    {"id":111, "pId":11, "name":"test111"}
];

$(function() {
    $.ajax({
        async   : false,
        cache   : false,
        type    : 'GET',
        dataType: "json",
        url     : "/menu",                                            //请求的action路径
        error   : function () {                                       //请求失败处理函数
            alert('数据请求失败');
        },
        success : function (data) {                                   //请求成功处理函数
            alert(data);
            treeNodes = data;                                         //把后台封装好的简单Json格式赋给treeNodes
        }
    });
    zTree = $("#tree").zTree(setting, treeNodes);
});