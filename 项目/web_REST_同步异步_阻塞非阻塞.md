- 同步异步: 体现在消息通知机制:需要client自己判断;
1. 同步体现在client自己等，然后过一段时间花费CPU去查看有没有response; 
2. 异步是client发出request之后就不管了，做别的事情，自己并不会花费什么去查看response, 而是response自己会以event/通知/回调函数的形式被return back; 
- 阻塞非阻塞: 是一种状态;具体是指：等待调用结果返回的时候的状态。实际上“阻塞非阻塞”的问题完整是“阻塞调用／非阻塞调用”
1. 阻塞调用: 调用结果返回之前, 该线程被挂起，调用线程在结果返回之后才会返回；
2. 非阻塞调用：当前线程调用并没有立刻得到结果，但是该线程不受影响，发出的调用不阻塞当前线程

详情: [怎样理解阻塞非阻塞与同步异步的区别](https://www.zhihu.com/question/19732473)

相关的:
1. [异步比同步快吗?](https://www.zhihu.com/question/269990607): 答案:不是的, 要看task是IO密集还是CPU密集;
2. IO密集: e.g. 网络，磁盘写入, etc. 
3. CPU密集: e.g. 图片处理啊、计算圆周率啊、视频解码 ...
4. 异步快的情况: IO密集型任务，很多时间都卡在等待上，这个时候异步会提高效率
5. 同步快的情况：CPU密集型任务，异步切来却去，保存、还原上下文等操作导致反而慢了



---
REST web services: synchronous or asynchrous?

实际上根本就没有关系: REST是一个标准，规范化HTTP call的过程； 而同步异步是请求资源的client的行为。

"Synchronous" or "Asynchronous" is the behaviour of the client that is requesting the resource. 
It has nothing to do with REST webservice, its structure, or the supporting server.

Synchronous behaviour:
- Client constructs an HTTP structure, sends over the socket connection.
- Waits for the response HTTP.

Asychronous behaviour:
- Client constructs HTTP structure, sends the request, and moves on.
- There's another thread that is waiting on the socket for the response. 
Once response arrives, the original sender is notified (usually, using a callback like structure).

REST web service is nothing but an HTTP call. You make a HTTP request to a URL and get a HTTP 
response back. How to handle the request and response is up to the caller.
