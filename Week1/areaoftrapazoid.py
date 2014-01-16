#Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area. The formula for the area of a trapezoid is:

#A = ½ * (x1 + x2) * h

#where A is the area, h is the height, and x1 and x2 are the top and bottom base of the trapezoid.

#Sample run:

#Area of a trapezoid

#Enter the height of the trapezoid: 5

#Enter the length of the bottom base: 10

#Enter the length of the top base: 7

#The area is: 42.5


trapazoid_height_int = int(input("Enter the height of the trapezoid: "))
trapazoid_length_bottom_int = int(input("Enter the length of the bottom base: "))
trapazoid_length_top_int = int(input("Enter the length of the top base: "))

trapazoid_area_int = ( .5 * (trapazoid_length_bottom_int + trapazoid_length_top_int) * trapazoid_height_int)

print('The area is:', trapazoid_area_int)
