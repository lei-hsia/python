### python2, python3区别:


### xrange

Python2使用xrange创建一个迭代器对象，使用range创建一个list数组

Python3使用range创建迭代器对象，移除了xrange: 就只是创建迭代器对象了

至于python2中的```xrange()```和```range()```的区别: 参考[这里:py2: xrange vs range](https://www.geeksforgeeks.org/range-vs-xrange-python/)
其实也就是4个区别: 
1. return type: ```xrange()``` returns a generator; ```range()``` returns a list;
2. memory: ```range > xrange```; 
3. operations: ```range```返回值是list, 所以所有list能用的ops都可以用在range返回值上; ```xrange```返回生成器对象，所以不仅只是遍历，还是只遍历一次，所以跟list相关的操作都不能用在xrange上面;
4. speed: ```xrange > range```;

python3 中的```range([start], stop)```: 从start开始，到stop，但是不包含stop

#### 编码

1. python2: 
- str: 已经编码后的字节序列(bytecode)
- unicode: 编码前的文本字符

2. python3:
- str: 编码过的unicode文本字符
- bytes: 编码前的字节序列(bytecode)

我们可以认为字符串有两种状态，即文本状态和字节（二进制）状态。Python2 和 
Python3 中的两种字符类型都分别对应这两种状态，然后相互之间进行编解码转化
编码就是将字符串转换成字节码，涉及到字符串的内部表示； 解码就是将字节码转换为字符串，将比特位显示成字符。

在 Python2 中，str 和 unicode 都有 encode 和 decode 方法； 但是不建议对 str 使用 encode，
对 unicode 使用 decode，这是 Python2 设计上的缺陷。(因为str本来就可以encode，但是2中的str是
字节序列，所以还可以decode; unicode本来可以decode，但是因为是文本字符，所以还可以encode);

Python3 则进行了优化，str 只有一个 encode 方法将字符串转化为一个字节码;而且 bytes 也只有一个 
decode 方法将字节码转化为一个文本字符串。

Python2中需要在文件头打上注释 # coding:utf-8 指定该程序使用的编码格式为UTF-8

#### print

Python2中的print是class, Python3中的print是函数

Python 2 的 print 声明已经被 print() 函数取代了, 意味着我们必须包装我们想打印在小括号中的对象。

所以我们输出格式为: 
```
print("")    # py3

print ""     # py2
print("")
```

#### input

1. python3: input解析输入为str字符型
2. python2: input解析输入为int型，raw_input解析输入为str类型
