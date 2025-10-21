colorlist=input("Enter a list of colors separated by comma: ").split(",")

colorlist=[color.strip() for color in colorlist]

print(f"First color: {colorlist[0]}")
print(f"Last color: {colorlist[-1]}")

