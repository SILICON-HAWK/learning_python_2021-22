list = [1,2,3,4,5,6,7,8,9]
count_even=0
count_odd=0
  
for num in list:

    if num % 2 == 0:
        count_even+=1
        print(num,'is a even number',',',count_even,'even numbers')
    elif num%2!=0:
        count_odd+=1
        print(num,'is a odd number',',',count_odd,'odd numbers')