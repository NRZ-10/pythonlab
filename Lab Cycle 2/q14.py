# Get input from the user
string = input("Enter a string: ")

# Check the ending and modify accordingly
if string.endswith("ing"):
    string = string + "ly"
else:
    string = string + "ing"

# Display the result
print("Modified string:", string)
