s = " ABCDEFGHBCDIJKLMNOPQRSBCDTUVWXYZ "
print("[", s, "]", sep="")
s = s.strip()
print("[", s, "]", sep="")
print(s.count("BCD"))
s = "ABCDEFGHIJK"
print(s)
for i in range(len(s)):
    print("[", s[i], "]", sep="", end="")
print()
for ch in s:
    print("<", ch, ">", sep="", end="")
print()
s = "ABCDEFGHIJK"
print(len(s) == s.__len__())
print('#',50*"-")