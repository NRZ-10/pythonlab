numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

positive_numbers = [n for n in numbers if n > 0]

squares = [n**2 for n in numbers]

word = input("Enter a word: ")

vowels = [ch for ch in word if ch.lower() in 'aeiou']

ordinal_values = [ord(ch) for ch in word]

print("\n--- Results ---")
print("Original numbers:", numbers)
print("Positive numbers:", positive_numbers)
print("Squares:", squares)
print("Word:", word)
print("Vowels in the word:", vowels)
print("Ordinal values:", ordinal_values)
