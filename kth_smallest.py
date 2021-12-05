def kthSmallest(arr, n, k):

    arr.sort()

    return arr[k-1]
  

arr = [12, 3, 5, 7, 19]
print
n = len(arr)
k = int(input("enter your the kth number you would like"))
print(k,"'th smallest element is", kthSmallest(arr, n, k))