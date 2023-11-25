# value =  0

# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value +=1

# value =  0

# while value <= 10:
#     value +=1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now " + str(value))

# names = ["Sarah", "Dave", "Jones", "Paul"]

# for name in names:
#     if name == "Dave":
#         break
#     print(name)

# for name in names:
#     if name == "Dave":
#         continue
#     print(name)

# for num in range(5, 101, 5):
#     print(num)
# else:
#     print("It's over!")

names = ["Sarah", "Dave", "Jones", "Paul"]
actions = ["eats", "codes", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")
