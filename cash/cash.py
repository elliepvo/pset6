from cs50 import get_int
from cs50 import get_float


change_owed = get_float("How much change do I owe: ")

if change_owed <= 0:
    change_owed = get_float("How much change do I owe: ")

change_owed = int(round(change_owed * 100))


qrt = change_owed // 25
dime = (change_owed % 25) // 10
nkl = ((change_owed % 25) % 10) // 5
remain = ((change_owed % 25) % 10) % 5

print(f"{qrt + dime + nkl + remain}")