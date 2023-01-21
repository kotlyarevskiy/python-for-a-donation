# Practical lesson No. 5, task No. 1.
# This program calculates the area of a rectangle.


def area_calculator(x, y):

	return x * y


def number_entry(side_name):

    while True:
        try:
            return int(input(f'Enter the numerical value of the {side_name} side.: '))
        except:
            print("That's not a valid option!")


x = number_entry('x')
y = number_entry('y')
S = area_calculator(x, y)
print(f'Area of the rectangle: {S}.')