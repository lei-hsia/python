##### numpy 复习

1. Numpy vs python原始类型: 为什么numpy那么快？
	a. 因为python中list分配内存的时候是不连续的，而numpy分配内存使用的是C/Fortran的连续内存地址，寻找的速度快
	b. Numpy的运算是矩阵运算，直接操作CPU

2. 逻辑读取都用pandas，numpy是处理数据用
3. 对元素的存储: 地址连续的两种方式:
	a. C:按行连续: 1,2,3,4,5,6,7,8
	b. Fortran:按列连续: 1,5,2,6,3,7,4,8

```
import numpy as np
a1 = np.array([1,2,3,4])
type(a1)

a2 = np.array([1,2,3],[4,5,6], dtype=np.int32)
a2.dtype
a2.shape #(2,3)

a3 = np.array([[[1,2,3],[4,5,6]], [[9,8,7],[5,4,3]]])
a3.shape  # (2,2,3)

a2.flags  # C/Fortran continuous
------------ ------------- ----------- ------------ -----------
np.ones([2,3])
np.zeros([2,3])

np.linspace(1, 100, 5)

np.random.rand(10)

# 二维数组的索引:先行后列:  获取第一个公司的前100天的涨跌幅情况
stock_day_rise[0][:100]  # 获取第一行(row:0)前100个数据
stock_day_rise[0, :100]  # 另一种获取第一行前100个数据的做法

# 获取前4个公司，前4天的涨跌幅情况
stock_day_rise[0:4, 0:4]  # 获取0,1,2,3行对应前4个公司，从开头到(不包含4)的涨跌幅情况

# 3维数组的索引: 获取第几张表，后面两个数对应获取的行数和列数
a[0, 0:4, 0:4] 
---------- ---------- ---------- ---------- ---------
# 改变形状: array.reshape(shape)  
stock_day.shape  # (500, 504)
stock_day.reshape([504,500])  # (504, 500)

# 修改数据类型: array.astype(type);  .dtype查看数据类型
stock.reshape([504.500]).dtype  # type('float32')
stock.reshape([504,500]).astype(int)  # type(int)

# 指定保留小数数位n: np.round(data, n)
np.round(stock_day[0:3, 0:4], 4)

------------------------------------------------------
numpy的相关计算:  1. 数据筛选运算; 2. 数据统计运算； 3. 数组间运算








```
