x = int
y = int
z= int
for x in (-10000,10000,1):
    for y in (-10000,10000,1):
        for z in (-10000,10000,1):
            if x + y*2 + z == 6:
                print (x,y,z)
            else:
                print("no sol")