class simplenet:
    def __init__(self,var1,var2):
        self.a = var1
        self.b = var2

    def sim(self,p):
        return self.a*p + self.b

net = simplenet(4.0,2.0)
print (net.sim(3.0))
print('#',50*"-")