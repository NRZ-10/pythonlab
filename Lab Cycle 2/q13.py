# Get input from the user
string = input("Enter a string: ")

# Create an empty dictionary to store character frequencies
char_freq = {}

# Count each character
for char in string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

# Display the result
print("Character frequencies:", char_freq)
