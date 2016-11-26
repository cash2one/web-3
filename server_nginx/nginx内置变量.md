###nginx内置变量
ngx_http_core_module————内置存放变量

#####客户请求title中的行
|         变量名          |                   含义                  |
|-------------------------|-----------------------------------------|
| ----------------------- | 请求头信息                              |
| $content_length         |                                         |
| $content_type           |                                         |
| $cookie_name            | cookie名称                              |
| $host                   | HTTP请求行的主机名（优先）              |
|                         | HOST请求头字段                          |
|                         | 服务器名                                |
| `$http_name`            | "name"可以替换成任意请求头字段          |
|                         | 将"-"替换为下划线                       |
|                         | 大写字母替换为小写                      |
| $http_referer           | 从哪个页面链接访问过来的                |
| $http_user_agent        | 客户浏览器的相关信息                    |
| $http_cookie            |                                         |
| $is_args                | 请求中是否有"?"/""                      |
| $arg_name               | 请求中的参数名（?arg_name="***"）       |
| $args                   | ==$query_string，请求中的参数值         |
| $http_x_forwarded_for   |                                         |
|-------------------------|-----------------------------------------|
| $remote_addr            | 客户端的ip地址                          |
| $remote_port            | 客户端port                              |
| $remote_user            | 客户端用户名                            |
| $binary_remote_addr     | 客户端地址的二进制形式（4字节）         |
| $proxy_protocol_addr    | 代理访问服务器的客户端地址              |
| $tcpinfo_rtt            | 客户端TCP连接的具体信息                 |
| $tcpinfo_rttvar         |                                         |
| $tcpinfo_snd_cwnd       |                                         |
| $tcpinfo_rcv_space      |                                         |
|-------------------------|-----------------------------------------|
| $document_uri           | ==$uri，当前request中的URI              |
| $request                | 请求的url与http协议                     |
| $request_body           | 请求体                                  |
| $request_body_file      | 保存客户端请求体的临时文件中            |
|                         | 文件处理结束后，此文件需删除            |
| $request_completion     | 请求是否成功，"ok"/""                   |
| $request_filename       | 当前请求的文件的路径                    |
|                         | 由root或alias和URI request组合而成      |
| $request_length         | 请求的长度                              |
|                         | 包括请求的地址、 http请求头和请求主体   |
| $request_method         | "GET"/"POST"                            |
| $request_time           | 处理客户端请求使用的时间                |
|                         | 从读取客户端的第一个字节开始计时        |
| $request_uri            | 含有参数的完整的初始URI                 |
| $scheme                 | "http"/"https"                          |
|-------------------------|-----------------------------------------|
| $document_root          | 当前请求的文档根目录或别名              |
| $realpath_root          | 当前请求的文档根目录或别名的真实路径    |
| $hostname               | 主机名                                  |
| $https                  | 是否开启SSL，"on"/""                    |
|-------------------------|-----------------------------------------|
| $limit_rate             | 设置响应的速度限制                      |
| `$sent_http_name`       | "name"可以替换成任意响应头字段          |
|                         | 将"-"替换为下划线                       |
|                         | 大写字母替换为小写                      |
| $server_addr            | 服务器端地址                            |
| $server_name            | 服务器名                                |
| $server_port            | 服务器的端口号                          |
| $server_protocol        | HTTP版本                                |
| $status                 | 响应代码，成功是200                     |
| $body_bytes_sent        | 传输给客户端的字节数（不计响应头）      |
| $bytes_sent             | 传输给客户端的字节数                    |
| $connection             | TCP连接的序列号                         |
| $connection_requests    | TCP连接当前的请求数量                   |
| $time_iso8601           | 访问服务器时间（ISO 8610格式）          |
| $time_local             | 访问服务器时间与时区（LOG Format 格式） |
|-------------------------|-----------------------------------------|
| $msec                   | 当前的Unix时间戳                        |
| $nginx_version          | nginx版本                               |
| $pid                    | 工作进程的PID                           |
| $pipe                   | 请求是否来自管道通信，"p"/"."           |


通常web服务器放在反向代理的后面，通过$remote_add拿到的IP地址是反向代理服务器的iP地址，这样就不能获取到客户的IP地址了

反向代理服务器在转发请求的http头信息中，可以增加x_forwarded_for信息，用以记录原有客户端的IP地址和原来客户端的请求的服务器地址