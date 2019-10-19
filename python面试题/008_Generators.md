#### Iterable
An ```iterable``` is any object in Python which has an ```__iter__``` or a 
```__getitem__``` method defined which returns an **iterator** or can take indexes. In
short an ```iterable``` is any object that provide us with an **iterator**.

#### Iterator
An iterator is any object in Python which has a ```next``` (Python2) or 
```__next__``` method defined. That’s it.

#### Generators

1. Generators are iterators, but can be iterated over just once
2. This is because they do not store all the values in memory, they generate values on the fly.
3. most of the time ```generators``` are implemented as functions. they do not ```return```
a value, then ```yield``` it.

Generators are best to calculate large sets of results, particularly calculations involving
loops themselves where you don't want to allocate the memory for al results at the same time.

https://www.zhihu.com/question/24807364

Python使用生成器对延迟操作提供了支持。所谓延迟操作，是指在需要的时候才产生结果，
而不是立即产生结果。这也是生成器的主要好处。

Python有两种不同的方式提供生成器：

1. 生成器函数：常规函数定义，但是，使用yield语句而不是return语句返回结果。
yield语句一次返回一个结果，在每个结果中间，挂起函数的状态，以便下次重它离开的地方继续执行
2. 生成器表达式：类似于列表推导，但是，生成器返回按需产生结果的一个对象，而不是一次构建一个结果列表

这个解释的非常清楚了: 
https://www.zhihu.com/question/24807364
