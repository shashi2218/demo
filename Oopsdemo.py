class calcultor:
    num = 100
    def __init__(self,a,b):
        self.firstno = a
        self.secondno = b
        print("i am called automatically when object is created")

    def getdata(self):
        print("I am now executing as method in class ")

    def summation(self):
        return self.firstno + self.secondno + self.num



obj = calcultor(2,5)
obj.getdata()
print(obj.summation())


obj1 = calcultor(4,8)
obj1.getdata()
print(obj1.summation())