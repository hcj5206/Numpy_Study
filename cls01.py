'''
NumPy中最重要的概念，NumPy数组。
'''
import numpy as np
my_array=np.array([1,2,3,4,5])
print(my_array.shape)
'''
生成0矩阵
'''
my_new_array = np.zeros((5))
print (my_new_array)
'''
随机矩阵,为每个元素分配0到1之间的随机值
'''
my_random_array = np.random.random((5))
print (my_random_array)
'''
二维矩阵 ,行，列
'''
my_2d_array = np.zeros((2, 3))
print(my_2d_array)
my_2d_array_1=np.array([
                        [1,2,3],
                        [2,3,4]
                    ])
print(my_2d_array_1)
print(my_2d_array_1[:,1]) # 第一列
print(my_2d_array_1[1,:]) # 第一行
