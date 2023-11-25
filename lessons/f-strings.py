person = "Dave"
coins = 3

dict = {"person": "Dave", "coins": 3}

print(f"{person} has {coins} coins left.")

print(f"{dict['person']} has {dict['coins']} coins left\n")

num = 2.25

for i in range(2, 10, 1):
    print(f"{i:.2f} multiplied by {num} is {(i * num):.2f}")
