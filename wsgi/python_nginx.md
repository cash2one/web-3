###uwsgi————类似一个桥接器，起到桥梁的作用
将nginx作为服务器最前端，它将接收WEB的所有请求，统一管理请求。nginx把所有静态请求自己来处理（这是NGINX的强项）。然后，NGINX将所有非静态请求通过uwsgi传递给Django，由Django来进行处理，从而完成一次WEB请求。

- pip install uwsgi
- uwsgi --version————查看 uwsgi 版本

###Django + uwsgi
uwsgi --http :8001 --chdir ${django目录} --wsgi-file ***/wsgi.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191

- http————协议类型和端口号
- workers————开启的进程数量，等同于processes
- stats————在指定的地址上，开启状态服务
- threads————运行线程。由于`GIL`的存在，没啥用
- daemonize————使进程在后台运行，并将日志打到指定的日志文件或者udp服务器（daemonize uWSGI）。实际上最常用的，还是把运行记录输出到一个本地文件上。
- pidfile————指定pid文件的位置，记录主进程的pid号
- wsgi-file————载入wsgi-file
- processes、chdir、master、vacuum————同myweb_uwsgi.ini文件参数