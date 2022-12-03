# Practical lesson No. 1, task No. 5.
# This program stores information about the cost of products that the user enters.

product_price = dict()

def stop_processing(check_str):

    proc_must_be_stopped = check_str == "stop"
    if proc_must_be_stopped:
        print(product_price)

    return proc_must_be_stopped

def add_data():

    first_input = input("Enter the name of a new or existing product or \"stop\" to stop entering data: ")
    if stop_processing(first_input):
        return

    second_input = input("Enter the price of the product in numbers or \"stop\" to stop entering data: ")
    if stop_processing(second_input):
        return

    product_price[first_input] = second_input
    add_data()


add_data()
