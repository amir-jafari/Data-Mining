def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = histogram('brontosaurus')
print(h)
def print_hist(h):
    for c in h:
        print( c, h[c])
h = histogram('parrot')
print_hist(h)
print('#',50*"-")