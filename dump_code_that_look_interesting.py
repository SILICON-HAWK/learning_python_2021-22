eg = [1,2,3,4,5,1,1,1]
eg.sort()
print(eg,'test for sort')
for x in eg:
    count=eg.count(x)
    print(x,"occurs", count,"times")
#converting the above list into an array

import array
array_eg=('i',eg)

print(array_eg,"conversion of list to array after sorting")
def remove_duplicate(arr):
    print('sorted array',arr)
    for f in arr:
        b=arr.count(f)
        if b!=0:
            arr.pop(b-1)

            print(arr,'new array')
    arr.append(0)

remove_duplicate(eg)



eg = [1,2,3,4,5,1,1,1]
eg.sort()
print(eg,'test for sort')
for x in eg:
    count=eg.count(x)
    print(x,"occurs", count,"times")
#converting the above list into an array

import array
array_eg=('i',[eg])

print(array_eg,"conversion of list to array after sorting")
def remove_duplicate(arr):

    print('sorted array',arr)
    for f in arr:
        b=arr.count(f)
        if b!=3:
            arr.pop(b-1)
            print(arr,'new array')

remove_duplicate(eg)


