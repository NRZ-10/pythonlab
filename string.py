text=input("Enter the text: ")
copies=int(input("Enter number of copies needed: "))
if copies<0:
    print("Enter a positive number: ")
else:
    result=text*copies
    print(result)

