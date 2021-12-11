num1=int(input("enther desired number 1 = "))
num2=int(input("enter desired number 2 = "))

print(num1 , num2, 'numbers before swapping')

num1= num1^num2

num2=num2^num1
num1=num1^num2

print(num1,num2, 'numbers after swap with xor')
