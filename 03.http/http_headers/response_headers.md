###响应头
#####第一行：HTTP/version-number status-code Reason-Phrase
- HTTP/version-number————HTTP协议的版本号；
- Status-Code————三个数字的状态码，主要用于机器自动识别，第一个数字定义响应的类别
    + 1xx————信息响应类————表示接收到请求并且继续处理；
    + 2xx————处理成功响应类————表示动作被成功接收、理解和接受；
    + 3xx————重定向响应类————为了完成指定的动作，必须接受进一步处理；
    + 4xx————客户端错误————客户请求包含语法错误或者是不能正确执行；
    + 5xx————服务端错误————服务器不能正确执行一个正确的请求；
- Reason-Phrase给Status-Code提供一个简单的文本描述，主要用于帮助用户理解。

|       Header       |                 作用                 |              示例             |
|--------------------|--------------------------------------|-------------------------------|
| Allow              | 实体头至服务器支持哪些请求方法       | GET,POST                      |
|                    | 不允许则返回405                      |                               |
| Accept-Ranges      | 是否允许获取某个（部分）资源         | bytes————接受                 |
|                    |                                      | none————不接受                |
| Server             | 指明HTTP服务器的软件信息             | Microsoft-IIS/7.5             |
| X-Powered-By       | 表示网站是用什么技术开发的           | ASP.NET                       |
| Transfer-Encoding  | 文件传输编码                         | chunked————分块               |
| Proxy-Authenticate | 代理服务器验证浏览器代理身份信息     |                               |
| Location           | 重定向接收者到一个新URI地址          |                               |
| Age                | 从原始服务器到代理缓存形成的估算时间 | （秒，非负）                  |
| Vary               | 使用缓存响应还是从原始服务器请求     | *                             |
| Content-Encoding   | 返回内容压缩编码类型                 | Content-Encoding: gzip        |
| Content-Language   | 响应体语言                           | en,zh                         |
| Content-Location   | 资源的备用地址                       |                               |
| Content-Range      | 指定返回体中某部分的字节位置         | bytes 21010-47021/47022       |
| Expires            | 指定浏览器本地缓存过期时间           | Tue, 08 Feb 2022 11:35:14 GMT |
|                    | （针对客户端）                       |                               |
| Last-Modified      | 资源的最后修改日期和时间             | Wed, 21 Dec 2011 09:09:10 GMT |
|                    | 客户端If-Modified-Since用它验证资源  |                               |
|                    | （针对客户端）                       |                               |
| ETag               | 当前请求变量的实体标签值             |                               |
|                    | 客户端If-Match用它验证资源           |                               |
|                    | （与客户端无关）                     |                               |