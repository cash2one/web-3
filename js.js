var table_id = "report_table";

var runObj = {
    '报单记录表': '080301',
    '新增房源明细表': '080302',
    '客户跟进明细表': '080303',
    '客户带看明细表': '080304',
    '新增客户明细表': '080305',
    'KPI数据报表': '080306'
};
var serviceObj = {
    '订单分配记录报表': '080307',
    '优办客户回访记录': '080308'
};
var officeObj = {
    '楼盘全量数据表': '080309'
};
var dataObj = {
    '虚拟号通话记录': '080310'
};

var createRow = function(objArray){
    var table = document.getElementById(table_id);
    function createCell(arg){
        var cell = row.insertCell();//创建一个单元
        cell.innerHTML = arg;
    }

    nameArray = new Array();
    buttonArray = new Array();
    for (i in objArray){
        for (j in objArray[i]){
            nameArray.push(j);
            var btnNumStr = objArray[i][j];
            var btnStr = '<button ' +
                'onclick="systemExportReportF(' + "'" + btnNumStr + "'" +
                ');" type="button" value="导出" class="btn btn-blue">' +
                '<i class="glyphicon glyphicon-export"></i>导出</button>';
            buttonArray.push(btnStr);
        }
    }
    for(i in nameArray){
        var row = table.insertRow();//创建一行
        createCell(nameArray[i]);
        createCell(buttonArray[i]);
    }
};


$(function() {
    $('[name=create_atBegin]').datepicker({
        format : 'yyyy-mm-dd',
        todayHighlight:true,
        todayBtn:'linked'
    });

    $('[name=create_atEnd]').datepicker({
        format : 'yyyy-mm-dd',
        todayHighlight:true,
        todayBtn:'linked'
    });


    var objArray = [runObj, serviceObj, officeObj, dataObj];
    createRow(objArray);
});


var serviceBtn = function(){
    $("#" + table_id).empty();
    objArray = [serviceObj];
    createRow(objArray);
};

var officeBtn = function(){
    $("#" + table_id).empty();
    objArray = [officeObj];
    createRow(objArray);
};

var dataBtn = function(){
    $("#" + table_id).empty();
    objArray = [dataObj];
    createRow(objArray);
};
