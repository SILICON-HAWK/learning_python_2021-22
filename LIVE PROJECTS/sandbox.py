print("select the action you would like to take")
print("1: for sphere")



def action_sphere(va):
    
    r = float(input('radius of the sphere'))
    if r<0:
        print('invalid argument select a positive number')
        action_sphere(va)
    else:
     print ('select your action','\n','1: for the volume of sphere')
     def volume_of_sphere(volume):

            print('the radius of the sphere is = ',r)
            import math
            print("the value of pi used is",math.pi)
            volume = ((math.pi)*(4/3)*r**3)
            print('the volume of sphere is',volume)

    ax=int(input())
    if ax==1:
      volume_of_sphere(input)
    else:
        print('invalid argument select one of the above option')
    return





print("2: for cube")
def function_cube(v):
    edge=float(input('input value for the length of cube'))
    if edge<0:
        print('invalid argument')
        function_cube(v)
    else:
        print('select your action','1: for the volume of cube')
        def volume_of_cube(v):
             print('the input value for the edge of the cube is=',edge)
             volume_of_cube = print('the volume of the cube = ',edge**3)
    bx = int(input())
    if bx==1:
        volume_of_cube(edge)
    else:
        print('invalid argument select one of the above action')
    




print("3: for fibonacchi sequence")
def fibonacchi_sequence(s):
    x,y=0,1
    limit=int(input('enter your upper limit for the sequence'))
    while y<limit:
        x,y=y,x+y
        print(y)
    return s





print("4: for cone")

def function_cone(r,h):
    
    r=float(input('input value of r'))
    h=float(input('input value of h'))
    if (r and h <0):
        print("invalid input")

    print ('select the action you would like to take','\n','1: for volume of cone','\n','2: for area of curved surface area')
    
    def volume_of_cone(r,h):
        c=(1/3)*(22/7)*(r**2)*h
        print("the value for r = ", r ," the value for h = ",h)
        print("the volume is",c)
        return c
    
    def curved_surface_area_of_cone(r,h):
        l=(r**2+h**2)**0.5
        area= (22/7)*r*l
        print('the area is',area)
        return area
    j=int(input())
    if j==1:
        volume_of_cone(r,h)
    if j==2:
        curved_surface_area_of_cone(r,h)





b=float(input("what action would you like to take"))

if b==1:
    action_sphere(input)
elif b==2:
    function_cube(input)
elif b==3:
    fibonacchi_sequence(input)
elif b==4:
    function_cone(input,input)
else:
    print('wrong input')