numbers=input("Enter a list of integers: ")
numberlist=numbers.split()
result=[]
for num in numberlist:
    n=int(num)
    if n>100:
        result.append("Over")
    else:
        result.append(n)
print(f"Processed list: {result}")
