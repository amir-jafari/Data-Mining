x = 1
print(dir(x))
print(x.__add__(3))
s = "abs"
print(s.__add__("Car"))
print(str.__add__(s, "Car"))
print('#',50*"-")
# -----------------------
word1 = 'Wow'
word2 = 'Wow'
print('Equal:',word1 == word2,
      ' Alias:',word1 is word2)
name = input("Please enter your name: ")
print("Hello " + name.upper() + ", how are you?")
word = "ABCD"
print(word.rjust(15, "*"))
print(word.rjust(15, ">"))
print(word.rjust(10)); print('#',50*"-")
# -----------------------
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
# -----------------------
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
print(t1.extend(t2));print(t2)
t = ['d', 'c', 'e', 'b', 'a']
print(t.sort()); print(t)
def add_all(t):
    total = 0
    for x in t:
        total += x
    return total
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
t = ['a', 'b', 'c']
x = t.pop(1); print(t)
s = 'spam'
print(list(s))
s = 'spam-spam-spam'
print(s.split('-')); print(s)
t = ['I', 'Love', 'Python', 'Very Much']
delimiter = ' '
print(delimiter.join(t))
print('#',50*"-")
# -----------------------
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
# -----------------------
def printall(*args):
    print (args)
printall(1, 2.0, '3')
t = (7, 3)
# divmod(t) --->Wrong
divmod(*t)
s = 'abc'
t = [0, 1, 2]
print(zip(s, t))
print(zip('Anne', 'Elk'))
print('#',50*"-")
# -----------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
pt = Point(2.5, 6)
print("(", pt.x, ",", pt.y, ")", sep="")
print('#',50*"-")
# -----------------------
class EmployeeRecord:
	def __init__(self, n, i, r):
		self.name = n
		self.id = i
		self.pay_rate = r

def open_database(filename, db):
    lines = open(filename)
    for line in lines:
        name, id, rate = eval(line)
        db.append(EmployeeRecord(name, id, rate))
    lines.close()
    return True

def print_database(db):
    for rec in db:
        print(str.format("{:>5}: {:<10} {:>6.2f}",
                         rec.id, rec.name, rec.pay_rate))

def less_than_by_name(e1, e2):
    return e1.name < e2.name

def less_than_by_id(e1, e2):
    return e1.id < e2.id

def less_than_by_pay(e1, e2):
    return e1.pay_rate < e2.pay_rate

def sort(db, comp):
    n = len(db)
    for i in range(n - 1):
        smallest = i

        for j in range(i + 1, n):
            if comp(db[j], db[smallest]):
                smallest = j
        if smallest != i:
            db[i], db[smallest] = db[smallest], db[i]
def main():
    database = []
    if open_database("data.dat", database):
        print("---- Unsorted:")
        print_database(database)
        sort(database, less_than_by_name)
        print("---- Name order:")
        print_database(database)
        sort(database, less_than_by_id)
        print("---- ID order:")
        print_database(database)
        sort(database, less_than_by_pay)
        print("---- Pay order:")
        print_database(database)
    else:  # Error, could not open file
        print("Could not open database file")
main()
print('#',50*"-")
# -----------------------
def a(x,y):
    print(x and y)

def o(x,y):
    print(x or y)
# -----------------------
import logic
logic.a(True, False)
logic.o(True, False)
print('#',50*"-")
# -----------------------
class simplenet:
    def __init__(self,var1,var2):
        self.a = var1
        self.b = var2

    def sim(self,p):
        return self.a*p + self.b

net = simplenet(4.0,2.0)
print (net.sim(3.0))
print('#',50*"-")
# -----------------------
x = int(input("Please enter a small positive integer: "))
print("x =", x)
try:
    x = int(input("Please enter a small positive integer: "))
    print("x =", x)
except ValueError:
    print("Input cannot be parsed as an integer")
print('#', 50 * "-")
# -----------------------
fout = open('output.txt', 'w')
print(fout)
line1 = "This is a file example,\n"
fout.write(line1)
line2 = "I am writing on a file.\n"
fout.write(line2)
fout.close()
print('#', 50 * "-")
# -----------------------
import os
cwd = os.getcwd()
print(cwd)
print(os.path.exists('output.txt'))
print(os.path.isdir('output.txt'))
print(os.listdir(cwd))
print('#', 50 * "-")
# -----------------------



