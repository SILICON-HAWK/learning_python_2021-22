basepay=int(input("input basepay of the user : "))

allowance=(50/100)*basepay

overtime=int(input('input users overtime per hour'))
overtimepay=1500*overtime

salary=basepay+allowance+overtimepay

print("the salary of the user is = ",salary)