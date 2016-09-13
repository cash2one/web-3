优点：
	减轻服务器的负担，按需取数据，最大程度的减少冗余请求；
	局部刷新页面，减少用户心理和实际的等待时间，带来更好的用户体验；
	基于xml标准化，并被广泛支持，不需安装插件等；
	进一步促进页面和数据的分离；
缺点：
	AJAX大量的使用了javascript和ajax引擎，这些取决于浏览器的支持，在编写的时候考虑对浏览器的兼容性；
	AJAX只是局部刷新，所以页面的后退按钮是没有用的；
	对流媒体还有移动设备的支持不是太好等。

var num = 0
$.ajax({
    url: '',
    type: 'post',
    async:false, //顺序执行，不异步执行
    data: {
    param1: var1, 
    param2: var2},
    success: function (data) {
        if (data.success == "ok") {
            num += 1
        }
        else if (data.success == "no") {
            num += 0
        }
    }
})

if (num > 0){
    window.location.reload();
}
