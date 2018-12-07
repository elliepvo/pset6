from cs50 import get_string
import sys


def main():

    # fulfill 2 arguments
    if len(sys.argv) != 2:
        print("Error \n")
        exit(1)

    # key as an integer
    k = int(sys.argv[1])

    if k < 0:
        print("Error \n")
        exit(1)

    # input plaintext
    print("plaintext: ")
    p = get_string()

    # print out ciphertext
    print("ciphertext: ", end="")

    # ciphertext function
    for i in range(len(p)):

        # ord returns an integer: ord(a) will return a value of 97
        # chr returns a character: chr(97) will return a value of 'a'
        # subtract base = 0, mod 26 to offset base = 0, add base back in for correct ASCII output
        # 97 is lowercase, 65 is uppercase, % 26 alphabet wrap

        if str.islower(p[i]):
            lower = (((ord(p[i]) + k) - 97) % 26) + 97
            print(chr(lower), end="")

        elif str.isupper(p[i]):
            upper = (((ord(p[i]) + k) - 65) % 26) + 65
            print(chr(upper), end="")

        else:
            print("{}".format(p[i]), end="")

    # prints ciphertext output
    print()


# allows ciphertext to work
if __name__ == "__main__":
    main()