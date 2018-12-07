# mario.c to mario.py

from cs50 import get_int

height = get_int("Positive integer: ")

while height < 0 or height > 23:
    height = get_int("Positive integer: ")
    if height == 0:
        height = get_int("Positive integer: ")

# write in hashes and spaces based on height input
for i in range(0, height):
    # going backwards from hash
    for spaces in range(0, height - i - 1):
        print(" ", end="")
    for hashes in range(0, i + 1):
        print("#", end="")

    for spaces in range(0, 1):
        print("  ", end="")

    for hashes in range(0, i + 1):
        print("#", end="")
    print()