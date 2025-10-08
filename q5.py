names=["niranjan", "mishal", "akshai", "aswin"]
count=0
for name in names:
    count += name.lower().count('a')

print(f"List of names:{names}")
print(f"Total occurence of 'a': {count}")
