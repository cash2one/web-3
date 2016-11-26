###uwsgi————类似一个桥接器，起到桥梁的作用
将nginx作为服务器最前端，它将接收WEB的所有请求，统一管理请求。nginx把所有静态请求自己来处理（这是NGINX的强项）。然后，NGINX将所有非静态请求通过uwsgi传递给Django，由Django来进行处理，从而完成一次WEB请求。

pip install uwsgi

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

#####uwsgi配置文件————将wsgi --***，给文件化
uwsgi支持多种类型的配置文件，如xml，ini
通过uwsgi命令读取uwsgi配置文件启动项目————uwsgi --ini myweb_uwsgi.ini

###uwsgi + nginx————配置nginx.conf
```
server {
    listen       uwsgi对外的端口号;
    server_name  网址/ip;
    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:8000; # 与uwsgi配置文件一致
        uwsgi_read_timeout 2;
    }
    location /static {
        expires 30d; autoindex on;
        add_header Cache-Control private;
        alias /home/www/mysite/static;
    }
}
```

静态请求：网址————请求————nginx————root/index
django网站：网址————请求————nginx————uwsgi————django