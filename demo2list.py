#lists
values = [1, 10, 'SHASHIDHAR', 22, 1997]

print(values[1])  #10

print(values[0])  #1
print(values[-1])  #1997
print(values[2])  #shashidhar
print(values[0:4])  #[1, 10, 'SHASHIDHAR', 22]
print(values[1:3])   #[10, 'SHASHIDHAR']

values.insert(2, 18)
print(values[0:4])  #[1, 10, 18, 'SHASHIDHAR']
values.insert(3, 'RAMPUR')
print(values)

values.append("ROHIT")
values[7] = 'rohit' #updating data in list
del values[0]   #deleting data in list
print(values)

#tuples
value = (1, 10, 'ROHIT', 22, 1997)
print(value[0])
print(value[2])
print(values)

#Dictionary

dic = {2:"shash", "palled":2, "age":3}
print(dic[2])
print(dic["palled"])

dict = {}

dict["firstname"] = "Rohit"
dict["lastname"] = "sharma"

dic["firstname"] = "Rohit"
dic["lastname"] = "sharma"
print(dic)
