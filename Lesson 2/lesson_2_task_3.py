import math 
 
def square(side): 
    square_area = side * side 
    return math.ceil(square_area) 
 
side = 4.5 
area = square(side) 
print("Площадь квадрата со стороной", side, "равна", area) 