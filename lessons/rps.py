import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def rps(name="Player"):
    player_wins = 0
    python_wins = 0
    game_count = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        nonlocal game_count

        user_choice = input(
            f"{name}, type one of the options:\n1 - Rock\n2 - Paper\n3 - Scissors\n\n"
        )

        if user_choice not in ["1", "2", "3"]:
            print(f"{name}, you have to input a number from 1 to 3.")
            play_rps()

        user_num = int(user_choice)

        python_choice = random.choice("123")
        python_num = int(python_choice)

        print(f"{name} chose: {str(RPS(user_num)).replace('RPS.', '')}.")
        print(f"Python chose: {str(RPS(python_num)).replace('RPS.', '')}.")

        def game_logic(user_num, python_num):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if user_num == 1 and python_num == 3:
                player_wins += 1
                return f"{name}, you win!"
            elif user_num == 2 and python_num == 1:
                player_wins += 1
                return f"{name}, you win!"
            elif user_num == 3 and python_num == 2:
                player_wins += 1
                return f"{name}, you win!"
            elif user_num == python_num:
                return "Tie game."
            else:
                python_wins += 1
                return "Python wins!"

        game_result = game_logic(user_num, python_num)
        game_count += 1

        print(game_result)
        print(f"Game count: {game_count}")
        print(f"{name} victories: {player_wins}")
        print(f"Python victories: {python_wins}")

        while True:
            opt = input(f"\n{name}, wanna play again?\n Y for yes \nN for no\n")

            if opt.lower() not in ["y", "n"]:
                print(f"\n{name}, you have to type Y or N")
                continue
            elif opt.lower() == "y":
                print("The game will start again!\n")
                play_rps()
            elif opt.lower() == "n":
                print(f"\n{name}, thanks for playing!\n")
                sys.exit()

    return play_rps()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized gaming experience."
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="Player's name.",
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
