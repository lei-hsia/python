同步异步: 是一种过程/机制/行为方式;
阻塞非阻塞: 是一种状态;

详情: [怎样理解阻塞非阻塞与同步异步的区别](https://www.zhihu.com/question/19732473)

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

