class JustNotCoolException(Exception):
    pass


x = 2

try:
    raise JustNotCoolException("Error test.")
    # raise Exception("Custom exception example!")
    # print(x / 1)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print("Variable undefined,")
except ZeroDivisionError:
    print("Division by zero.")
except Exception as error:
    print(error)
else:
    print("No errors!")
finally:
    print("print with or without a error")
