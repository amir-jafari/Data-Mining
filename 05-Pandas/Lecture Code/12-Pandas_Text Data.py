import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series(['Amir', 'Brian James', 'Luo', '@gmail','1234','AmirJafari'])
print(s)
print(s.str.lower())
print(s.str.upper())
print(s.str.len())
print(s.str.strip())
print(s.str.split(' '))
print(s.str.cat(sep='-'))
print(s.str.get_dummies())
print(s.str.contains('@'))
print(s.str.replace('@','-'))
print(s.str.count('m'))
print(s.str. startswith ('A'))
print(s.str.endswith('4'))
print('#',50*"-")