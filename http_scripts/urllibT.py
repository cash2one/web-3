# coding:utf-8
# 1)urlencode函数，可以把key-value键值对转换成我们想要的格式，返回a=1&b=2这样的字符串。
from urllib import urlencode
data = {
	'a': 'test',
	'name': '魔兽'
}
code1 = urlencode(data)
print code1
# 2)urllib提供另外一个函数：quote()，只对一个字符串进行urlencode转换。
from urllib import quote
code2 = quote('魔兽')
print code2
# 3)unquote()接受urlencode之后传递过来的字符串进行解码！
from urllib import unquote
print unquote(code1)
print unquote(code2)

# urlencode就是把字符串转成gbk编码，然后把\x替换成%。如果你的终端是utf8编码的，那么要把结果再转成utf8输出，否则就乱码。unquote()这个函数的输出，是对应中文在gbk下的编码。