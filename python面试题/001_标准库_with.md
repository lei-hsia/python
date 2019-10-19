1. 列出 5 个常用 Python 标准库？
```
import os    # 操作系统接口  示例：os.system('ls')
import sys   # 命令行参数    示例：sys.path
import re
import math
import time
import random
import threading
import multiprocessing
```
...
https://www.zhihu.com/question/54513391

2. with 方法打开处理文件帮我们做了什么? 

- with 语句适用于对资源进行访问的场合， 确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源, 比如文件使用后自动关闭，线程中锁的自动获取和释放；
－ with是context manager; 在程序中表示代码执行过程中所处的前后环境; 
- context manager: [here](https://book.pythontips.com/en/latest/context_managers.html); 
- 含有```__enter__```和```__exit__```方法的对象就是context manager;
- ```__enter__()```: 执行语句之前，首先执行这个方法, 通常返回一个实例对象;
- ```__exit()__```: 执行语句结束后，自动调用```__exit()__```, 用户释放资源;

Implementing a Context Manger as a Class:
```
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()
```
Just by defining ```__enter``` and ```__exit__``` methods, we can use our new class in 
a ```with``` statement. Let's try:

```
with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hallo')
```
What happened underhood: 

1. ```with``` statement stores the ```__exit``` method of the ```File``` class;
2. It calls the ```__enter__``` method of the ```File``` class;
3. The ```__enter__``` method opens the file and returns it;
4. The opened file handle is passed to ```opened_file```.
5. We write to the file using ```.write()```.
6. The ```with``` statement calls the stored ```__exit__``` method.
7. The ```__exit__``` method closes the file.

