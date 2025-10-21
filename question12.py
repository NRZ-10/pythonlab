numbers= list(map(int,input("Enter list of integers: ").split()))

noteven=[num for num in numbers if num % 2 != 0]

print(f"List after removing even numbers: {noteven}")

