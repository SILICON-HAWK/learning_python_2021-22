list=[1,2,3,4,5,6,"banana","cat","dog","tree"]
x = len(list)
print(list)
print("the list length is = ",x)
list.insert(4,15)
print(list,"list after using insert")
list.remove("cat")
print(list,"list after using remove")
list.pop(9)
print(list,"list after using pop")
del list
print(list,"after using del")