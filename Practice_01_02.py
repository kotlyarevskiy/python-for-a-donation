# Practical lesson No. 1, task No. 2.
# This program determines the number of characters in a line that the user types
# and prohibits input of lines that are longer than 20 characters.

input_string = input("Enter a string that is no more than 20 characters long: ")
string_len = len(input_string)
if string_len > 20:
    print(f"WARNING! You have entered more than 20 characters ({string_len})!!!")
else:
    print(input_string)
