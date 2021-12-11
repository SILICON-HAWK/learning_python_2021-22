terms = [1,2,3,4,5,6,7,8,9]
list1 = []
for val in range(0,terms,1):
    n = int(input("Enter integer : "))
    list1.append(n)
    print("Circulating the elements of list",list1)
for val in range(0,terms,1):
    n = list1.pop(0)
    list1.append(n)
    print(list1)