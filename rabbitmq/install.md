###MQ（Message Queue）———— 消息队列（MQ）
- 一种应用程序对应用程序的通信方法；
- 应用程序通过读写出入队列的消息（数据）来通信；

消息传递指的是程序之间通过在消息中发送数据进行通信，而不是通过直接调用彼此来通信，直接调用通常是用于诸如远程过程调用的技术。
排队指的是应用程序通过队列来通信。队列的使用除去了接收和发送应用程序同时执行的要求。

MQ是消费-生产者模型的一个典型的代表，一端往消息队列中不断写入消息，而另一端则可以读取或者订阅队列中的消息。
MQ和JMS类似，但不同的是JMS是SUN JAVA消息中间件服务的一个标准和API定义，而MQ则是遵循了AMQP协议的具体实现和产品。

在项目中，将一些无需即时返回且耗时的操作提取出来，进行了异步处理，而这种异步处理的方式大大的节省了服务器的请求响应时间，从而提高了系统的吞吐量。

RabbitMQ是一个在AMQP基础上完整的，可复用的企业消息系统。他遵循Mozilla Public License开源协议。

###AMQP协议
AMQP 有四个非常重要的概念：
虚拟机(virtual host)，通道(exchange)，队列(queue)和绑定(binding)。
虚拟机————通常是应用的外在边界，我们可以为不同的虚拟机分配访问权限。虚拟机可持有多个交换机、队列和绑定。
交换机————从连接通道(Channel)接收消息，并按照特定的路由规则发送给队列。
队列————消息最终的存储容器，直到消费客户端(Consumer)将其取走。
绑定————也就是所谓的路由规则，告诉交换机将何种类型的消息发送到某个队列中。

RabbitMQ是一个消息代理。它的核心原理非常简单：接收和发送消息。
你可以把它想像成一个邮局：你把信件放入邮箱，邮递员就会把信件投递到你的收件人处。在这个比喻中，RabbitMQ是一个邮箱、邮局、邮递员。RabbitMQ和邮局的主要区别是，它处理的不是纸，而是接收、存储和发送二进制的数据——消息。

[进阶学习](https://www.rabbitmq.com/tutorials/amqp-concepts.html)、[官网](http://www.rabbitmq.com/features.html)

1>可靠性(Reliability)
    RabbitMQ提供很多特性供我们可以在性能和可靠性作出折中的选择，包括持久化、发送确认、发布者确认和高可用性等。
2>弹性选路(Flexible Routing)
    消息在到达队列前通过交换（exchanges）来被选路。RabbitMQ为典型的选路逻辑设计了几个内置的交换类型。对于更加复杂的选路，我们可以将exchanges绑定在一起或者写属于自己的exchange类型插件。
3>集群化(Clustering)
    在一个局域网内的几个RabbitMQ服务器可以集群起来，组成一个逻辑的代理人。
    http://www.360doc.com/content/14/0911/17/15077656_408713893.shtml

###RabbitMQ

#####安装rabbitMq
1. rabbit是用erlang写的，要先装erlang环境；
2. 环境变量：
    ```
    ERLANG_HOME=${Erlang_dir}
    path+=%ERLANG_HOME%\bin;
    ```
3. 安装[RabbitMQ服务器软件](http://www.rabbitmq.com/java-client.html)；
4. 环境变量：
    + RABBITMQ_SERVER=${RabbitMQ Server}
    + path+=%RABBITMQ_SERVER%\sbin;
5. 安装celery————调用rabbitMq的消息队列用的；
6. 启动消息队列服务器rabbitmq；
7. 启动执行任务线程；
8. 编写任务去执行

#####Rabbit自带监控功能————(网页控制台)[http://localhost:15672]，用户名和密码都是guest
|      cmd脚本（%RABBITMQ_SERVER%\sbin）      |                         作用                        |
|---------------------------------------------|-----------------------------------------------------|
| rabbitmq-server.bat                         | 启动rabbitmq                                        |
| rabbitmq-plugins.bat list                   | 查看已安装的插件列表                                |
| rabbitmq-plugins enable rabbitmq_management | 启用网页控制台监控管理                              |
| rabbitmq-server on                          | 打开server                                          |
| rabbitmqctl status                          | 查询节点状态（Status of node 'rabbit@WORKGROUP-1'） |

（一）用户管理 
用户管理包括增加用户，删除用户，查看用户列表，修改用户密码。
1>新增一个用户
  rabbitmqctl  add_user  Username  Password 
2>删除一个用户 
  rabbitmqctl  delete_user  Username 
3>修改用户的密码
  rabbitmqctl  change_password  Username  Newpassword 
4>查看当前用户列表
  rabbitmqctl  list_users 
（二）用户角色 
按照个人理解，用户角色可分为五类，超级管理员, 监控者, 策略制定者, 普通管理者以及其他。
1>超级管理员(administrator) 
  可登陆管理控制台(启用management plugin的情况下)，可查看所有的信息，并且可以对用户，策略(policy)进行操作。 
2>监控者(monitoring) 
  可登陆管理控制台(启用management plugin的情况下)，同时可以查看rabbitmq节点的相关信息(进程数，内存使用情况，磁盘使用情况等) 
3>策略制定者(policymaker) 
  可登陆管理控制台(启用management plugin的情况下), 同时可以对policy进行管理。但无法查看节点的相关信息(上图红框标识的部分)。 
4>普通管理者(management) 
  仅可登陆管理控制台(启用management plugin的情况下)，无法看到节点信息，也无法对策略进行管理。
5>其他(None)
  无法登陆管理控制台，通常就是普通的生产者和消费者。 
（三）设置角色
  1>命令为：rabbitmqctl  set_user_tags  User  Tag 
    User为用户名， Tag为角色名(对应于上面的administrator，monitoring，policymaker，management，或其他自定义名称)。
    也可以给同一用户设置多个角色，例如 rabbitmqctl  set_user_tags  hncscwc  monitoring  policymaker 
（四）用户权限([-p  VHostPath] 为虚拟机名称。具体不清楚这种怎么用,我的用法是1.网页端设置 2.使用另一种也就是5设置虚拟机和权限)
  1>用户权限指的是用户对exchange，queue的操作权限，包括配置权限，读写权限。配置权限会影响到exchange，queue的声明和删除。读写权限影响到从queue里取消息，向exchange发送消息以及queue和exchange的绑定(bind)操作。 
  2>例如： 将queue绑定到某exchange上，需要具有queue的可写权限，以及exchange的可读权限；向exchange发送消息需要具有exchange的可写权限；从queue里取数据需要具有queue的可读权限。详细请参考官方文档中"How permissions work"部分。
  3>相关命令如下：
    1)设置用户权限
      rabbitmqctl  set_permissions  -p  VHostPath  User  ConfP  WriteP  ReadP 
    2)查看(指定hostpath)所有用户的权限信息 
      rabbitmqctl  list_permissions  [-p  VHostPath] 
    3)查看指定用户的权限信息 
      rabbitmqctl  list_user_permissions  User 
    4)清除用户的权限信息 
      rabbitmqctl  clear_permissions  [-p VHostPath]  User 
5.设置虚拟机和权限(这里设置完的权限是归属于你创建的虚拟机)
参考：http://www.cnblogs.com/daizhj/archive/2010/10/21/1857374.html


虚拟机(基于sbin目录下)：
  1>首先创建vhosts，命令如下：
    rabbitmqctl add_vhost dnt_mq   
  2>删除虚拟机
    rabbitmqctl delete_vhost vhostpath
  3>显示出所有虚拟主机信息
    rabbitmqctl list_vhosts
添加用户名和密码：
  1>添加用户和密码(用户名ayf, 密码:pwd):
    rabbitmqctl add_user ayf pwd
  2>修改用户密码
    rabbitmqctl change_password username newpassword
权限设置:
  1>绑定用户权限
    rabbitmqctl set_permissions -p dnt_mq ayf ".*" ".*" ".*"
  2>列出用户权限
    rabbitmqctl list_user_permissions ayf
  3>清除用户权限
    rabbitmqctl clear_permissions [-p vhostpath] username
