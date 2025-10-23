n1 = int(input("Enter number of items in first dictionary: "))
dict1 = {}
for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

n2 = int(input("\nEnter number of items in second dictionary: "))
dict2 = {}
for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

merged_dict = dict1.copy()      # make a copy of dict1
merged_dict.update(dict2)       # add items from dict2

print("\nFirst Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged_dict)
