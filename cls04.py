'''
-*- coding: utf-8 -*-
@Author  : HCJ
@Time    : 2019-09-02 10:46
@Software: PyCharm
@File    : cls04.py
'''
'''
numpy中的矩阵和向量
'''

import numpy as np

'''
向量只是具有单列的数组。 例如，构建向量
更方便的方法是转置相应的行向量。 例如，为了使上面的矢量，我们可以改为转置行向量
'''
v = np.array([[2],[1],[3]])
v2 = np.transpose(np.array([[2,1,3]]))
'''
用numpy求解方程组
'''
A = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
b = np.transpose(np.array([[-3,5,-2]]))
x = np.linalg.solve(A,b)
print(x)
