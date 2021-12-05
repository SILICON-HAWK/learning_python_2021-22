print("select the action you would like to take")
print("1: for finding the volume of sphere")

def sphere(set):
    r = float(input('radius of the sphere'))
    def volume_of_sphere(v):
        if r<0:
            print('input invalid, input a positive number')
        else:
            print('the radius of the sphere is = ',r)
            import math
            print("the value of pi used is",math.pi)
            volume = ((math.pi)*(4/3)*r**3)
            print(volume)
        return v
    def surface_area_sphere(a):
        if r<0:
            print('input invalid, input a positive number')
        else:
            print('the radius of the sphere is = ', r)
            import math
            print('the radius of the sphere is = ',r)

print('2: for vol of cube')
def cube(v):
    edge=float(input('input the side length of the cube'))
    if edge<0:
        print("input invalid, input a positive number")
    else:
        print('the input value for the edge of the cube is=',edge)
        volume_of_cube=print(edge**3)
    return v 




b = int(input())
if b==1:
 sphere(input)
if b==2:
    cube(input)
else:
    print("select a valid")