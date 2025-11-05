# main.py
from Armstrong import is_armstrong

# Input limits from user
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

print(f"Armstrong numbers between {lower} and {upper}:")
for num in range(lower, upper + 1):
    if is_armstrong(num):
        print(num)
