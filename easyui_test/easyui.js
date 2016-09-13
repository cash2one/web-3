/*
* @Date:   2016-08-04 10:59:28
* @Last Modified time: 2016-08-26 10:02:19
*/

var getGroupName = function(){
    /**
     * 通过组织架构控件选择的部门
     * @type {string}
     */
    var depIds  = '';
    var depNames = '';
    var checkedNodes = $('#departmentUserComboxTree_new').combotree('tree').tree('getChecked');
    for (var i=0; i<checkedNodes.length; i++){
        {
            if (checkedNodes[i].children.length == 0) {
                var parentNode = $('#departmentUserComboxTree_new').combotree('tree').tree('getParent', checkedNodes[j].target);
                if(parentNode != null){
                    depNames += parentNode.text + '|' + checkedNodes[i].text + ',';
                } else {
                    depNames += checkedNodes[i].text + ',';
                }
            }
            depIds += checkedNodes[i].id + ',';
        }
    }
    if(depIds.length > 1){
        var groupIds = depIds.substring(0, depIds.length-1);
    }
    return groupIds;
};