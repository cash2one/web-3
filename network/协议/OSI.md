###OSI/RM————Open System Interconnection/Reference Model————开放系统互连参考模型
为了使不同计算机厂家生产的计算机能够相互通信，以便在更大的范围内建立计算机网络，国际标准化组织（ISO）在1978年提出的。

#####开放系统————遵循OSI参考模型和相关协议能够实现互连的具有各种应用目的的计算机系统。

#####层次结构
- 不同开放系统中相同层的实体为同等层实体；
- 同等层之间的通信规则和约定称之为协议，同等层实体之间通信由该层的协议管理；
- 相同层间的接口定义了原语操作和低层向上层提供的服务；
- 所提供的公共服务是面向连接的或无连接的数据服务；

由于网络节点之间联系的复杂性，在制定协议时，通常把复杂成分分解成一些简单成分，然后再将它们复合起来。最常用的复合技术就是层次方式，网络协议的层次结构如下：

- 结构中的每一层的功能是独立的，规定有明确的服务及接口标准。每层完成所定义的功能，修改本层的功能并不影响其他层。
- 把用户的应用程序作为最高层。
- 除了最高层外，中间的每一层都向上一层提供服务，同时又是下一层的用户。把如何实现这一服务的细节对上一层加以屏蔽，并与其他层的具体实现无关。
- 把物理通信线路作为最低层，它使用从最高层传送来的参数，是提供服务的基础。直接的数据传送仅在最低层实现。

通常把1～4层协议称为下层协议，5～7层协议称为上层协议。

osi参考模型每层都是有特定的功能，从上到下层层独立。看协议和设备属于哪一层，都要看这个协议或者设备涉及到了哪几层，涉及到的最靠上的那一层就是这个协议或设备所在层。

####分层————从低到高
第一层，物理层（Physical Layer），传输比特流，即二进制（“0”或“1”）的信号。

比特传输必须依赖于传输设备和物理媒体，但是，物理层不是指具体的物理设备，也不是指信号传输的物理媒体，而是指在物理媒体之上为上一层（数据链路层）提供一个传输原始比特流的物理连接。

第二层，数据链路层（Datalink Layer）传输帧，从物理层接收的数据进行MAC地址（网卡的地址）的封装与解封装。

它控制网络层与物理层之间的通信。它的主要功能是如何在不可靠的物理线路上进行数据的可靠传递。
为了保证传输，从网络层接收到的数据被分割成特定的可被物理层传输的帧。帧是用来移动数据的结构包，它不仅包括原始数据，还包括发送方和接收方的物理地址以及纠错和控制信息。其中的地址确定了帧将发送到何处，而纠错和控制信息则确保帧无差错到达。如果在传送数据时，接收点检测到所传数据中有差错，就要通知发送方重发这一帧。
一方面接收来自网络层（第三层）的数据帧并为物理层封装这些帧；另一方面数据链路层把来自物理层的原始数据比特封装到网络层的帧中。
该层的作用包括：物理地址寻址、数据的成帧、流量控制、数据的检错、重发等。
数据链路层的协议包括：SDLC、HDLC、PPP、STP、帧中继等。

第三层，网络层（Network Layer）传输数据包，将从下层接收到的数据进行IP地址的封装与解封装。
其主要功能是将网络地址翻译成对应的物理地址，并决定如何将数据从发送方路由到接收方。网络层通过综合考虑发送优先权、网络拥塞程度、服务质量以及可选路由的花费来决定从一个网络中节点Ａ 到另一个网络中节点Ｂ 的最佳路径。
网络层是可选的，它只用于当两个计算机系统处于不同的由路由器分割开的网段这种情况，或者当通信应用要求某种网络层或传输层提供的服务、特性或者能力时。


第四层，传输层（Transport Layer）传输段或报文，定义了一些传输数据的协议和端口号（WWW端口80等）。
主要是将从下层接收的数据进行分段进行传输，到达目的地址后在进行重组。常常把这一层数据叫做段。


第五层，会话层，通过传输层（端口号：传输端口与接收端口）建立数据传输的通路。在分开的计算机上的两种应用程序之间建立一种虚拟链接，这种虚拟链接称为会话（session）。会话层通过在数据流中设置检查点而保持应用程序之间的同步。允许应用程序进行通信的名称识别和安全性的工作就由会话层完成。主要在你的系统之间发起会话或或者接受会话请求（设备之间需要互相认识可以是IP也可以是MAC或者是主机名）。

第六层，表示层。定义由应用程序用来交换数据的格式。在这种意义上，表示层也称为转换器（translator）。主要是进行对接收的数据进行解释、加密与解密、压缩与解压缩等（也就是把计算机能够识别的东西转换成人能够能识别的东西（如图片、声音等））。
加密分为链路加密和端到端的加密。对于表示层，参与的加密属于端到端的加密，指信息由发送端自动加密，并进入TCP/IP数据包封装，然后作为不可阅读和不可识别的数据进入互联网。到达目的地后，再自动充足解密，成为可读数据。

第七层，应用层，为应用程序提供服务以保证通信，但不是进行通信的应用程序本身。

纵观七层，从低级到高级，从汇编到了BASIC，越到高层与硬件的关联就越弱。

###七层模型在Windows程序下的体现
- 物理层————网卡————把线路发送过来的高频电流转化数据包，然后传给网卡驱动程序，同是也把网卡驱动程序传送过来的数据包转化成电信号传送出去。定义通过网络设备发送数据的物理方式：是网络媒介和设备间的接口。
- 数据链路层————网卡驱动程序。定义控制通信连接的程序；封包；监测和改正包传输错误。
- 网络层————NDIS————提供网络接口，决定网络设备间如何传输数据；根据唯一的网络设备地址选择包；提供流和拥塞控制，以阻止同时网络资源的损耗。
- 传输层————TCP————进行TCP协议的封包处理。管理网络中首尾连接的信息传送；提供通过错误恢复和流控制装置传送可靠且有序的包；提供无连接面向包的传送。
- 会话层————SPI————服务提供者接口，管理用户间的会话和对话；控制用户间的连接和挂断连接；报告上层错误。
- 表示层————API————为应用程序提供接口。API负责SPI与应用程序之间的通信；定义不同体系间不同数据格式；具体说明独立结构的数据传输格式；编码和解码数据；加密和解密数据；压缩和解压缩数据。
- 应用层————EXE————应用程序。定义用于网络通信和数据传输的用户接口程序；提供标准服务，比如虚拟终端、文档以及任务的传输和操作。