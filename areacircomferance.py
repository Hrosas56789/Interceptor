'''
Hector Rosas
18/8/16
Area and Circumference of a circle

input radius using the keyboard
'''

pi = 3.14
radius_circle = float(input("Enter the Radius of the Circle :"))
area_circle = pi*radius_circle**2
circumference_circle = 2*pi*radius_circle

print('Area of a circle of radius', radius_circle, 'm is :',area_circle + "Square meters")
print("Circumference of the circle is :" , circumference_circle)