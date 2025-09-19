string=input("Enter a string: " )
if len(string)>1:
    new_string=string[-1]+string[1:-1]+string[0]
else:
    new_string=string
print(f"String after exchanging first and last character: {new_string}")
