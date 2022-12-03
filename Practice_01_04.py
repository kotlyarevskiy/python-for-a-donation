# Practical lesson No. 1, task No. 4.
# This program determines the area of a circle based on the user-entered radius.
import math

input_radius = int(input("Enter the radius value to calculate the area of the circle: "))
area = round(input_radius * math.pi ** 2, 2)
print(f"The area of a circle with a radius of {input_radius} is {area}.")