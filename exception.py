itemsincart =2

if itemsincart !=2:# raise Execption("error ")
    pass

assert (itemsincart==2)


try:
    with open('test.txt', 'r') as reader:
        reader.read()
except:
    print("s")

#or to get python error follow below steps

try:
    with open('test.txt', 'r') as reader:
        reader.read()
except Exception as s:
    print(s)

finally:
    print("cleaning up records")
