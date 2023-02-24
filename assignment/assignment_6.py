'''
For your assignment, please use the code below first and then write your code.
DO NOT DELETE THE FOLLOWING CODE
'''

import sys
try:
    input = sys.argv[1]
    input2 = sys.argv[2]
except:
    print("You didn't put any input when you run your code! Please add an input!")
    input = ""
    input2 = ""

'''
The objective of this assignment is to print the expected output.
You can find it in the instruction folder.
List of installed and authorized packages :
    - numpy
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
import numpy as np
input = [int(i) 
if i.isdigit() 
else i for i in input.split(',')]
input2 = [int(i) 
if i.isdigit()
else i for i in input2.split(',')]
print(np.array([input, input2]).T)