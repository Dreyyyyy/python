import os

f = open("files/names.txt")

# print(f.read(4))

# print(f.readline())

# for line in f:
#     print(line)

# f.close()

# try:
#     f = open("files/names.txt")
# except:
#     print(f"Error while open the file")
# finally:
#     f.close()

# f = open("files/names.txt", "a")

# f.write("\nNeil")
# f.close()

# f = open("files/names.txt", "r")

# print(f.read())

# f.close()

# f = open("files/names.txt", "w")

# f.write("I've deleted all the files")
# f.close()

# f = open("files/names.txt", "r")

# print(f.read())

# f.close()

# if not os.path.exists("dave.txt"):
#     f = open("files/dave.txt", "x")
#     f.close()

# if os.path.exists("files/dave.txt"):
#     os.remove("files/dave.txt")
# else:
#     print("The file doesn't exist.")

with open("files/more-names.txt", "r") as f:
    f.read()

with open("files/names.txt", "w") as f:
    f.write("Andrey")
