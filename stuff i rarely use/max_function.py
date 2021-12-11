list1 = ["Ram", "rem", "Kiran"]
list2 = [4,24,45,36,76,46]


max_1=max(list1,key=len)
max_2=max(list2)


print(max_1,'max in list 1')
print(max_2,'max in list 2')

for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')