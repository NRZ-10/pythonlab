string=input("Enter a string: ");
first_char=string[0]
new_string=first_char + string[1:].replace(first_char, '$')
print(f"Modified string : {new_string}")

