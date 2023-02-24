'''
For your assignment, please use the code below first and then write your code.
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
import numpy as np
import sklearn 
from sklearn import linear_model
try:
    input1 = sys.argv[1]
    input2 = sys.argv[2]
except:
    print("You didn't put any input when you run your code! Please add an input!")
    input1 = ""
    input2 = ""


'''
The objective of this assignment is to print the expected output.
You can find it in the instruction folder.
List of installed and authorized packages :
    - numpy
    - scikit-learn (import sklearn)
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
input1 = [int(i) for i in input1.split(',')]
input2 = [int(i) for i in input2.split(',')]

arr_x = np.array(input1)
arr_y = np.array(input2)

Xm = np.mean(arr_x)
Ym = np.mean(arr_y)

ss = 0
sp = 0

for i in arr_x:
    ss += (i - Xm)**2

for (i, j) in zip(arr_x,arr_y):
    sp += (i - Xm)*(j - Ym)


b = sp / ss

w1 = Ym - (b * Xm)


# use this printing (where "w1" is the weight and "b" the bias)
print("The most accurate linear regression has the following equation: y' = {:0.2f}*x + {:0.2f}".format(b, w1))