u = input("Give me a number: ")
try:
    n = float(u)
    if n.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    pass