# Practical lesson No. 1, task No. 3.
# The program determines the possibility of the existence of a triangle
# by the length of its sides, which are entered by the user.

a, b, c = \
    int(input("Enter the side A length: ")), \
    int(input("Enter the side B length: ")), \
    int(input("Enter the side C length: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("A triangle with such sides does not exist!!!")
else:
    print("Such a triangle exists!!!")