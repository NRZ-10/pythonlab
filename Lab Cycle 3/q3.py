n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    numbers.append(element)

sum = 0

for num in numbers:
    sum = sum + num

print("The sum of all items in the list is:", sum)
