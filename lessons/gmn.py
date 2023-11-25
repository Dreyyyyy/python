import sys
import random


def gmn(name="Player"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_gmn():
        nonlocal game_count
        nonlocal player_wins
        nonlocal python_wins
        nonlocal name

        num_guess = input(f"\n{name}, guess the number I'm thinking (from 1 to 3):\n")

        if num_guess not in ["1", "2", "3"]:
            print(f"\n{name}, you have to guess a number between 1 to 3:\n")
            play_gmn()
        else:

            def game_logic():
                nonlocal player_wins
                nonlocal python_wins
                nonlocal name

                py_guess = random.choice("123")
                if num_guess == py_guess:
                    player_wins += 1
                    return f"\n{name}, you win!\n\n"
                else:
                    python_wins += 1
                    return f"\n{name}, you lose :(\n\n"

        game_result = game_logic()
        game_count += 1

        print(game_result)
        print(f"{name} wins: {player_wins}")
        print(f"Python wins: {python_wins}")
        print(
            f"{name} win percentage: {((int(player_wins) / game_count) * 100):.2f}%.\n"
        )

        while True:
            opt = input(
                f"{name}, do you want to continue to play?\nY for yes\nN for no\n"
            )

            if opt.lower() not in ["y", "n"]:
                print(f"{name}, you have to type Y or N.\n")
                continue
            else:
                if opt.lower() == "y":
                    play_gmn()
                else:
                    sys.exit(f"{name}, thanks for playing!")

    return play_gmn()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized gaming experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="Player's name"
    )

    args = parser.parse_args()

    guess_my_number = gmn(args.name)
    guess_my_number
