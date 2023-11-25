import math

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Cofee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# Numeric data types

# Integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# Complex value
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in function for numbers
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zip_code = "100001"
zip_value = int(zip_code)
print(type(zip_value))

# Error if you attempt to cast incorrect type data
# value = int("New York")
