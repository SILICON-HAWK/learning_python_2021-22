print("select the action you would like to take")
print("1: for finding the volume of sphere")
print('2: for vol of cube')

def sphere(set):
    r = float(input('radius of the sphere'))
    print('type 1 for volume of sphere')
    print('type 2 for area of sphere')
    k=int(input('select you input'))
    if r<0:
        print('input invalid, input a positive number')
    
    else:
        if k==1:
            def volume_of_sphere(v):

                print('the radius of the sphere is = ',r)
                import math
                print("the value of pi used is",math.pi)
                volume = ((math.pi)*(4/3)*r**3)
                print(volume)
            return
        elif k==2:
            def surface_area_sphere(a):

                print('the radius of the sphere is = ', r)
                import math
                print('the radius of the sphere is = ',r)
                area=((4)*(math.pi)*(r**2))
                print (area)
            return  

def cube(v):
    edge=float(input('input the side length of the cube'))
    print('type 1 for volume of cube')
    print('type 2 for area of the cube')
    k=int(input('select your action'))
    if edge<0:
        print("input invalid, input a positive number")
    else:

        if k ==1:
            def volume_of_cube(v):
                print('the input value for the edge of the cube is=',edge)
            volume_of_cube_1=print((edge**3))
            return
        elif k==2:
            def surface_area_cube(a):
                print('the input value for the edge of the cube is = ',edge)
            surface_area_cube_1=print((6)*(edge**2))
            return surface_area_cube
        else:
            print('input valid command')
            return cube   #error response, send back to start



b = int(input())
if b==1:
 sphere(input)
if b==2:
    cube(input)
else:
    print("select a valid")