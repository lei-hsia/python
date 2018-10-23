协程是python个中另外一种实现多任务的方式，只不过比线程更小占用更小执行单元（理解为需要的资源）。 为啥说它是一个执行单元，<b>因为它自带CPU上下文</b>。这样只要在合适的时机， 我们可以把一个协程 切换到另一个协程。 只要这个过程中保存或恢复 CPU上下文那么程序还是可以运行的。

通俗的理解：在一个线程中的某个函数，可以在任何地方保存当前函数的一些临时变量等信息，然后切换到另外一个函数中执行，注意不是通过调用函数的方式做到的，并且切换的次数以及什么时候再切换到原来的函数都由开发者自己确定

协程和线程差异

在实现多任务时, 线程切换从系统层面远不止保存和恢复 CPU上下文这么简单。 操作系统为了程序运行的高效性<b>每个线程都有自己缓存Cache等等数据，操作系统还会帮你做这些数据的恢复操作</b>。 所以线程的切换非常耗性能。但是协程的切换只是单纯的操作CPU的上下文，所以一秒钟切换个上百万次系统都抗的住。

1. multi-threading: (concurrency)
	when 2 or more tasks can start, run, and complete in overlapping time periods. It does not necessarily mean they are de facto running at the same time, but within, say 1 second, there's millions of execution of them and you see them AS IF they're running at the same time, but in fact only one of them is running on CPU at a time. For instance, multitasking on a single-core machine.
	
2. multi-processing: (parellelism)
	when tasks literally run at the same time, e.g. on a multicore processor, multi-processing