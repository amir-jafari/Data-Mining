def permute(prefix, suffix):
    suffix_size = len(suffix)
    if suffix_size == 0:
        print(prefix)
    else:
        for i in range(0, suffix_size):
            new_pre = prefix + [suffix[i]]
            new_suff = suffix[:i] + suffix[i + 1:]
            permute(new_pre, new_suff)
def print_permutations(lst):
    permute([], lst)
def main():
    a = [1, 2, 3, 4]
    print_permutations(a)
main()
print('#',50*"-")