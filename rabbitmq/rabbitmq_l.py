# encoding:utf-8
from amqplib import client_0_8 as amqp
conn = amqp.Connection(host='localhost:5672', userid='guest',
                       password='guest', virtual_host='/', insist=False)
chan = conn.channel
'''
每个channel都被分配了一个整数标识，自动由Connection()类的.channel()方法维护。
或者，你可以使用.channel(x)来指定channel标识，其中x是你想要使用的channel标识。
通常情况下，推荐使用.channel()方法来自动分配channel标识，以便防止冲突。

现在我们已经有了一个可以用的连接和channel。
现在，我们的代码将分成两个应用，生产者（producer）和消费者（consumer）。
我们先创建一个消费者程序，他会创建一个叫做“po_box”的队列和一个叫“sorting_room”的交换机：
'''
chan.queue_declare(queue='po_box', durable=True,  # 队列——Queue
                   exclusive=False, auto_delete=False)

chan.exchange_declare(exchange='sorting_room', type='direct', durable=True,  # 交换机——exchange
                      auto_delete=False)
'''
创建一个名叫“po_box”的队列，
它是durable的（重启之后会重新建立），
并且最后一个消费者断开的时候不会自动删除（auto_delete=False）。

在创建durable的队列（或者交换机）的时候，将auto_delete设置成false是很重要的，
否则队列将会在最后一个消费者断开的时候消失，与durable与否无关。

如果将durable和auto_delete都设置成True，只有尚有消费者活动的队列可以在RabbitMQ意外崩溃的时候自动恢复。

（你可能注意到了另一个标志，称为“exclusive”。
如果设置成True，只有创建这个队列的消费者程序才允许连接到该队列。
这种队列对于这个消费者程序是私有的）。



还有另一个交换机声明，创建了一个名字叫“sorting_room”的交换机。
auto_delete和durable的含义和队列是一样的。

但是，.excange_declare() 还有另外一个参数叫做type，
用来指定要创建的交换机的类型（如前面列出的）： fanout, direct 和 topic.



到此为止，你已经有了一个可以接收消息的队列和一个可以发送消息的交换机。
不过我们需要创建一个绑定，把它们连接起来。
'''


chan.queue_bind(queue='po_box', exchange='sorting_room',
                routing_key='jason')


'''
这个绑定的过程非常直接。
任何送到交换机“sorting_room”的具有路由键“jason” 的消息都被路由到名为“po_box” 的队列。

现在，你有两种方法从队列当中取出消息。
第一个是调用chan.basic_get()，主动从队列当中拉出下一个消息
（如果队列当中没有消息，chan.basic_get()会返回None，
因此下面代码当中print msg.body 会在没有消息的时候崩掉）：
'''


msg = chan.basic_get('po_box')
print msg.body
chan.basic_ack(msg.delivery_tag)


'''
但是如果你想要应用程序在消息到达的时候立即得到通知怎么办？
这种情况下不能使用chan.basic_get()，你需要用chan.basic_consume()注册一个新消息到达的回调。
'''
