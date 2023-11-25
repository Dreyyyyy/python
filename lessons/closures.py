def parent_function(person, coins):
    def play_game():
        nonlocal coins
        coins -= 1
        if coins > 0:
            print(person + " has " + str(coins) + ".")
        else:
            print(person + " out of coins.")

    return play_game


tommy = parent_function("Tommy", 4)
jenny = parent_function("Jenny", 2)

tommy()
tommy()

jenny()
