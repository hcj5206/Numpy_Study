'''
-*- coding: utf-8 -*-
@Author  : HCJ
@Time    : 2019-09-02 10:19
@Software: PyCharm
@File    : cls03.py
'''
'''
创建Numpy数组的不同方式
'''
import numpy as np
'''
arange是一种广泛使用的函数，用于快速创建数组。将值20传递给arange函数会创建一个值范围为0到19的数组。
'''
array = np.arange(20)      #和range差不多 start end step
print(array)

'''
创建一个二维数组
'''
array = np.arange(20).reshape(4,5)
print(array)
print(array[1])
'''
 创建三维数组及更多维度
'''
array = np.arange(27).reshape(3,3,3)
print(array)
print(array.shape)
'''
使用其他Numpy函数 创建数组
np.zeros((2,4)) 填充零
np.ones((3,4)) ones函数创建一个填充了1的数组。
np.empty((2,3)) empty函数创建一个数组。它的初始内容是随机的，取决于内存的状态。
np.full((2,2), 3)  full函数创建一个填充给定值的n * n数组
np.eye(3,3) eye函数可以创建一个n * n矩阵，对角线为1s，其他为0。
np.linspace(0, 10, num=4) 函数linspace在指定的时间间隔内返回均匀间隔的数字。 例如，下面的函数返回0到10之间的四个等间距数字。
'''
ar=np.zeros((3,3,4))
print(ar)