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

np.ones([2,3])
np.zeros([2,3])

np.linspace(1, 100, 5)

np.random.rand(10)


```