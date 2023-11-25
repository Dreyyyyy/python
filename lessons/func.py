def hello_world():
    print("Hello world!")


def sum(num1=0, num2=0):
    if type(num1) is not int or type(num2) is not int:
        return
    return num1 + num2


hello_world()

res = sum(1, 6)
print(res)


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", last="Grey")
