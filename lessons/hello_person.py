def hello(name, lang):
    dict = {"English": "Hello", "Portuguese": "Olá", "Spanish": "Holla"}
    print(f"{dict[lang]} {name}!")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personal greeting.")

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person to greet.",
    )

    parser.add_argument(
        "-l",
        "--lang",
        metavar="language",
        required=True,
        choices=["English", "Portuguese", "Spanish"],
        help="The language of the greeting.",
    )

    args = parser.parse_args()

    hello(args.name, args.lang)
