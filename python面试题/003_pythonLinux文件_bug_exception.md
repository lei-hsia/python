#### python删除文件, linux删除;
```
# python 
import os
os.remove("demo.txt")

# linux
rm demo.txt
```

#### 自定义异常: 
```
# coding: utf-8

def judge_value(num_value):
  """自定义异常函数
  
  自定义异常函数, 用于抛出大于一定值的异常
  :param num_value: 用于判断的值
  :return: 异常信息
  """
  if num_value > 10:
      # raise用于抛出自定义异常, 格式: raise 异常类型(异常注明) 
      # 一旦触发之后不再执行raise后面的代码 
      raise ValueError("数量不能大于10")
  else:
      return "200"
      
if __name__ == "__main__":
    judge_value(10)
```

#### 举例说明异常模块中 try except else finally 的相关意义
```
# coding: utf-8

def read_data(file_name):
    """读取文件数据
    
    读取指定文件中的所有数据， 返回数据或者异常信息
    :param file_name: 文件路径
    :return: 文件数据或者异常信息
    """
    file_obj = ""
    try:
        #
        file_obj = open(file_name, "r") # 打开file之后放进file_obj,相当于序列化为string
        res_data = file_obj.read() # 然后这个string通过read方法得到res
    except IOError as e: 
        file_obj = "文件不存在："+str(e)
    else: 
        return res_data
    finally:
        # 不管有没有error都会执行的代码
        if isinstance(file_obj, str):
            return file_obj
        else isinstance(file_obj, file):
            file_obj.close()
        else: 
            return "未知错误，请检查您的代码..."

if __name__ == "__main__":
    res = read_data("abc.txt")
    print(res)
```

