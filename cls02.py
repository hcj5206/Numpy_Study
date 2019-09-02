
'''
NumPy中的数组操作 加减乘除 点乘
+ - * /
'''
from __future__ import print_function

import numpy as np

a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
sum = a + b
difference = a - b
product = a * b
quotient = a / b
matrix_product = a.dot(b)
print("Sum = \n", sum )
print("Difference = \n", difference )
print("Product = \n", product ) # 逐项相乘
print("Quotient = \n", quotient)
print ("Matrix Product = ", matrix_product)

