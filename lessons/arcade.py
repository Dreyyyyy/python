import sys

from rps import rps
from gmn import gmn


def arcade(name="Player"):
    opt = input(
        f"\nHello {name}, please, choose your game:\n\n1 - Rock, Paper, Scissors,\n2 - Guess My Number,\n3 - Quit\n\n"
    )

    if opt not in ["1", "2", "3"]:
        print(f"\nPlease {name}, choose a option from 1 to 3.\n")
        arcade()
    else:
        if opt == "1":
            print("Starting Rock, Paper, Scissors...\n")
            rps(name)
        elif opt == "2":
            print("Starting Guess My Number...\n")
            gmn(name)
        else:
            sys.exit(f"\n{name}, thanks for playing!\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personalized interface.")

    parser.add_argument(
        "-n", "--name", metavar="name", required=False, help="Player's name"
    )

    args = parser.parse_args()

    if args.name:
        arcade_launch = arcade(args.name)
    else:
        arcade_launch = arcade()
    arcade_launch
