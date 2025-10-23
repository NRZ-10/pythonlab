n = int(input("Enter number of items in the dictionary: "))
my_dict = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    my_dict[key] = value

asc_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

desc_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("\nOriginal Dictionary:", my_dict)
print("Ascending Order:", asc_dict)
print("Descending Order:", desc_dict)
