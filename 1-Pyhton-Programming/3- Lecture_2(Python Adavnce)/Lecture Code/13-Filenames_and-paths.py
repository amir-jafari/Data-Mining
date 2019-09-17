import os
cwd = os.getcwd()
print(cwd)
print(os.path.exists('output.txt'))
print(os.path.isdir('output.txt'))
print(os.listdir(cwd))
print('#', 50 * "-")