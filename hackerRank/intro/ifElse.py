# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

userIn = input(int())

if (userIn%2!=0):
    print("Weird")

else:
    if 2 <= userIn <= 5:
        print("Not Weird")
    if 6<= userIn <=20:
        print("Weird")
    else:
        print("Not Weird")