import math

side_of_length = int(input())
number_of_sides = int(input())

area_of_regular_polygon = (number_of_sides * side_of_length * side_of_length) 
area_tan = 4*math.tan (math.pi/number_of_sides)

area_of_regular_polygon = "{:.2f}".format(area_of_regular_polygon / area_tan)

print(area_of_regular_polygon)