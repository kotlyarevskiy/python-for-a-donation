# Practical lesson No. 1, task No. 1.
# This program displays the data entered by the user on the screen.

name, middle_name, lastname = \
    str(input("Enter your name: ")), \
    str(input("Enter your middle name: ")), \
    str(input("Enter your last name: "))

print("Hello, " + name + " " + middle_name + " " + lastname + "!")
