import os
import re

path = os.getcwd()

with open(os.path.join(path,'text.txt'), 'r') as f:
    data = f.read()

numbers = re.findall(r'\d+', data)
summ = sum(map( lambda x: int(x), numbers))
print(summ)