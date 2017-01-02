/**
 * Created by ZDD on 2016/12/26.
 */

/**
 * setting————zTree的参数配置————JSON对象
 */
var setting = {
    //数据是否采用简单Array格式，默认false
    isSimpleData : true,
    //在isSimpleData格式下，当前节点键名称
    treeNodeKey : "id",
    //在isSimpleData格式下，当前节点的父节点键名称
    treeNodeParentKey : "pId",
    //
    //是否显示节点间的连线
    showLine : true,
    //每个节点上是否显示 CheckBox
    checkable : true,
    //

    data: {
        simpleData: {
            enable: true
        }
    }
};


/**
 * zTreeNodes————zTree的全部节点数据集合————JSON数组
 */
var zTreeNodes = [
    {name: ''}
];


/**
 * zTree(setting, [zTreeNodes])
 */
var zTree;
$(function() {
    zTree = $("#tree").zTree(setting, treeNodes);
});