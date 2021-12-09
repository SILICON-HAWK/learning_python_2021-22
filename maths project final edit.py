#Final
import math
def volume_of_cone(r,h):                         #BY 21BCE10077
    c=(1/3)*(math.pi)*(r**2)*h
    return c
def curved_surface_area_of_cone(r,h):
    l=(r**2+h**2)**0.5
    area= (math.pie)*r*l
    return area
def total_surface_area_of_a_cone(r,h):
    l=(r**2+h**2)**0.5
    area=(math.pie)*r*(l+h)
    return area




def sphere(set):                                #BY21BCE10074
    import math
    r = float(input('radius of the sphere'))
    print("Select")
    print('1. for volume of sphere')
    print('2. for area of sphere')
    k = int(input('select you input'))
    if r < 0:
        print('input invalid, input a positive number')

    else:

        if k == 1:
            volume_of_sphere_ = print(((math.pi) * (4 / 3) * r ** 3))
            print('this is the value of volume of given sphere')

        elif k == 2:
            area_of_sphere_ = print(((4) * (math.pi) * (r * r)))
            print('this is the value of area of given sphere')


def cube(v):
    edge = float(input('input the side length of the cube'))
    print("select:")
    print('1.volume of cube')
    print('2. area of the cube')
    k = int(input('select your action'))
    if edge < 0:
        print("input invalid, input a positive number")
    else:

        if k == 1:
            def volume_of_cube(v):
                print('the input value for the edge of the cube is=', edge)

            volume_of_cube_1 = print((edge ** 3))
            return
        elif k == 2:
            def surface_area_cube(a):
                print('the input value for the edge of the cube is = ', edge)

            surface_area_cube_1 = print((6) * (edge ** 2))
            return surface_area_cube
        else:
            print('input valid command')
            return cube






def hemisphere_area(r):                                #By 21BCG10140
  a=3*(22/7)*r*r
  return a
def hemisphere_volume(r):
  v=(2/3)*(22/7)*r*r*r
  return v
def cubiod_volume(l,b,h):            #BY
    volume =l*b*h
    return volume
def Total_surface_area_of_cubiod_(l,b,h):
    a=2*(l*b+b*h+l*h)
    return a
def lateral_surface_area_of_cuboid(l,b,h):
    q= 2*h*(l+b)
    return q





print("select the action you would like to take",'\n',"1.cude",'\n',"2.cone",'\n',"3.sphere",'\n',"4.Hemisphere",'\n',"5.cubiod")
b = int(input("Enter:"))
if b==1:
    cube(input)
if b==2:

    print("select:"'\n',"1.Curved surface area of cone",'\n',"2.Total surface area of cone",'\n',"3.Volume of cone")
    s=int(input("Enter your choose:"))
    if s==1:
        r=float(input("Enter radius:"))
        h=float(input("Enter height"))
        print("Curved surface area of cube =",curved_surface_area_of_cone(r,h))
    elif s==2:
        r = float(input("Enter radius:"))
        h = float(input("Enter height"))
        print("Total surface area of cone==",total_surface_area_of_a_cone(r,h))
    elif s==3:
        r = float(input("Enter radius:"))
        h = float(input("Enter height"))
        print("volume of cone==",volume_of_cone(r,h))
if b==3:
    sphere(input)
if b==4:
    print("select:"'\n', "1.Area of hemisphere", '\n', "2.Volume of hemisphere", '\n')
    y=int(input("Enter :"))
    if y == 1:
        x = float(input("Enter radius of the hemisphere "))
        print("THE AREA IS:")
        print(hemisphere_area(x))
    elif y == 2:
        x = float(input("Enter radius of the hemisphere "))
        print("THE VOLUME IS")
        print(hemisphere_area(x))
if b==5:
     print("select:"'\n',"1.lateral surface  of cuboid",'\n',"2.Total surface area of cuboid",'\n',"3.Volume of cone")
     w=int(input("Enter: "))
     if w==1:
         l=float(input("Enter lenth:"))
         b=float(input("Enter depth:"))
         h = float(input("Enter height:"))
         print("lateral surface  of cuboid=",lateral_surface_area_of_cuboid(l,b,h))

     if w==2:

        l = float(input("Enter lenth:"))
        b = float(input("Enter depth:"))
        h = float(input("Enter height:"))
        print("lateral surface  of cuboid=", Total_surface_area_of_cubiod_(l,b,h))

     if w==3:
        l = float(input("Enter lenth:"))
        b = float(input("Enter depth:"))
        h = float(input("Enter height:"))
        print("volume  of cuboid=", cubiod_volume(l,b,h) )





