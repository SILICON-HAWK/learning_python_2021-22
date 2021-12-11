
def cone(r,h):
    import math
    r=float(input("Enter radius:"))
    h=float(input("Enter height"))
    print("select:"'\n',"1.Curved surface area of cone",'\n',"2.Total surface area of cone",'\n',"3.Volume of cone")
    s=int(input("Enter your choose:"))
    if s==3:
        def volume_of_cone(r,h):                         #BY 21BCE10077
            c=(1/3)*(math.pi)*(r**2)*h
            return c
        print("volume of cone==",volume_of_cone(r,h))
    if s==1:    
        def curved_surface_area_of_cone(r,h):
            l=(r**2+h**2)**0.5
            area= (math.pi)*r*l
            return area
        print("Curved surface area of cube =",curved_surface_area_of_cone(r,h))
    if s==2:    
        def total_surface_area_of_a_cone(r,h):
            l=(r**2+h**2)**0.5
            area=(math.pi)*r*(l+h)
            return area
        print("Total surface area of cone==",total_surface_area_of_a_cone(r,h))

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
    print('1. volume of cube')
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

def hemisphere(r):
    print("select:"'\n', 
    "1.Area of hemisphere",
    '\n',
    "2.Volume of hemisphere",
    '\n')
    y=int(input("Enter :"))
    x = float(input("Enter radius of the hemisphere "))


    if y==1:
     def hemisphere_area(r):                                #By 21BCG10140
         a=3*(22/7)*r*r
         print("THE AREA IS:")
         print(hemisphere_area(x)) 
         return a
    

    if y==2:
     def hemisphere_volume(r):
         v=(2/3)*(22/7)*r*r*r
         print("THE VOLUME IS")         
         print(hemisphere_volume(x))
         return v
 
def cuboid(l,b,h):
    w=int(input("Enter: "))
    l=float(input("Enter lenth:"))
    b=float(input("Enter depth:"))
    h = float(input("Enter height:"))
    if w==1:
        def cubiod_volume(l,b,h):                               #BYxxxxxxxxxxxx
            volume =l*b*h
            print("volume  of cuboid=", cubiod_volume(l,b,h))
            return volume
    if w==2:    
        def Total_surface_area_of_cubiod_(l,b,h):
            a=2*(l*b+b*h+l*h)
            print("lateral surface  of cuboid=", Total_surface_area_of_cubiod_(l,b,h))
            return a
    if w==3:    
        def lateral_surface_area_of_cuboid(l,b,h):
            q= 2*h*(l+b)
            print("lateral surface  of cuboid=",lateral_surface_area_of_cuboid(l,b,h))
            return q


while True:
    print("select the action you would like to take",
    '\n',
    "1.cube",
    '\n',
    "2.cone",
    '\n',
    "3.sphere",
    '\n',
    "4.Hemisphere",
    '\n',
    "5.cubiod"
    '\n',
    "6.exit")
    b = int(input("Enter:"))
    if b==1:
        cube(input)

    if b==2:
        cone(input,input)

    if b==3:
        sphere(input)

    if b==4:
        hemisphere(input)

    if b==5:
        cuboid(input,input,input)
    
    if b==6:
        break
    else:
        print('invalid option, select appropriate option')