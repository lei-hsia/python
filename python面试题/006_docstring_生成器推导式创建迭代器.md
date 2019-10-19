DocStrings 文档字符串是一个重要工具，用于解释文档程序，帮助你的程序文档更加简单易懂。

可以在函数体的第一行使用一对三个单引号 ''' 或者一对三个双引号 """ 来定义文档字符串。
可以使用 __doc__（注意双下划线）调用函数中的文档字符串属性。

DocStrings文档字符串使用惯例：它的首行简述函数功能，第二行空行，第三行为函数的具体描述。

```
# coding:utf-8

def create_iterator(list_param):
    """创建迭代器
    
    使用生成器推导式创建一个迭代器, 并返回迭代器
    :param list_param: 迭代对象
    :return: 迭代器
    """
    # 将列表推导式的[]改成()即为生成器推导式，众所周知，生成器返回一个迭代器对象
    return (value for value in list_param)
    
if __name__ == "__main__":
    # 遍历迭代器
    for i in create_iterator([1,2,3]):
        print(i)
    
    # 使用__doc__输出函数中的文档字符串属性
    print(create_iterator.__doc__)
    # 使用__dir__输出函数中的所有属性和方法
    print(create_iterator.__dir__)
```

