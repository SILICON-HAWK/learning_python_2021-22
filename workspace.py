import array 

arr=array.array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
def partition_function(k):
    import array
    new_array1=array.array('i')
    new_array2=array.array('i')
    for i in arr:
        k=int(10)
        if i > 10:
            new_array1.append(i)
        else:
            new_array2.append(i)
        
    print(new_array1)
    print(new_array2)

partition_function(10)