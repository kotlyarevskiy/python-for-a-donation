# Practical lesson No. 2, task No. 2.
# This program calculates the factorial of a number entered by the user.

while True:
    try:
        user_input = int(input('Enter an integer: '))
        break
    except:
        print("That's not a valid option!")

factorial = 1
while user_input > 1:
    factorial *= user_input
    user_input -= 1

print(factorial)

