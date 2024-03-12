from Oopsdemo import calcultor


class childcalcultor(calcultor):
    num2 = 200

    def __init__(self):
        calcultor.__init__(self,2,10)

    def getcompletedata(self):
        return self.num + self.num2 + self.summation()


obj = childcalcultor()
print(obj.getcompletedata())
