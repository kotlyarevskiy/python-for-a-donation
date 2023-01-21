# Practical lesson No. 5, task No. 1.
# This program checks the value of a global variable.



def glob_checkingor():

    def glob_is_positive():
        print(f'Global varieble is positive!')

    def glob_is_negative():
        print(f'Global varieble is negative!')

    if (g > 0):
        glob_is_positive()
    elif (g < 0):
        glob_is_negative()
    else:
        print(f'Global varieble is 0!')



def number_entry():

    while True:
        try:
            return int(input(f'Enter the numerical value of the global value side: '))
        except:
            print("That's not a valid option!")


g = number_entry()

glob_checkingor()
