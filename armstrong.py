num = int(input("Enter a number: "))
sum_of_powers=0
order=len(str(num))
temp = num

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit**order
    temp //= 10

if num == sum_of_powers:
 print(f"{num} is an armstrong number")
else:
 print(f"{num} is not an armstrong number")


