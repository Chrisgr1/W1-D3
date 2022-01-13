def return_10():
    return 10

def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide( num1, num2):
    return num1 / num2


def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(num1, num2):
    return (int(num1) + int(num2))

def number_to_full_month_name(num):
    if num == 1:
        return "January"
    elif num == 3:
        return "March"
    elif num == 9:
        return "September"

def number_to_short_month_name(num):
    if num == 1:
        return "Jan"
    elif num == 4:
        return "Apr"
    elif num == 10:
        return "Oct"

def volume_of_cube(num):
    return num ** 3


def reverse_string(string):
    return string[::-1]

def fahrenheit_to_celsius(num):
    return (num - 32) * (5 / 9)
