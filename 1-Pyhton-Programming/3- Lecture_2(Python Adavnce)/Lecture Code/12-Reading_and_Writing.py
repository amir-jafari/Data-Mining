fout = open('output.txt', 'w')
print(fout)
line1 = "This is a file example,\n"
fout.write(line1)
line2 = "I am writing on a file.\n"
fout.write(line2)
fout.close()
print('#', 50 * "-")