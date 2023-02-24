'''
The objective of this assignment is to print the dataframe showed in the instruction.
Only one test will be done.
You can write you code after this comment :
'''
#Your code here:
import pandas as pd
names = ["Brad", "Angelina", "Tom"]
surnames = ["Pitt", "Jolie", "Cruise"]
ages = [58, 47, 60]

df = pd.DataFrame(list(zip(names, surnames, ages)), columns = ["Name", "Surname", "Age"])
print(df)

