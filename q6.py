list1=list(map(int, input("Enter first list of integers: ").split()))
list2=list(map(int, input("Enter second list of integers: ").split()))

if len(list1) == len(list2):
    print("Both list are of same length.")
else:
    print("List are of different length.")

if sum(list1) == sum(list2):
    print("Both list have same sum")
else:
    print("Both list don't have same sum")

commonvalues = set(list1) & set(list2)

if commonvalues:
    print(f"Commom values found: {commonvalues}")
else:
    print(f"Commom values not found")

