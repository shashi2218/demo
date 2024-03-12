file = open('test.txt')
#print(file.read(2))
#print(file.read(5))

#print((file.readline()))
#print((file.readline()))

#-------------------------------#
#1st method to read using readline with while loop

#line = file.readline()
#while line!="":
 #   print(line)
  #  line=file.readline()

#2nd method to read using readlines with for loop

for line in file.readlines():
    print(line)

file.close()
