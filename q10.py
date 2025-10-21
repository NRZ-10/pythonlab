colorlist1=input("enter colors for list1 : ").split()
colorlist2=input("enter colors for list2 : ").split()

result=[color for color in colorlist1 if color not in colorlist2]
print(f"Color from cololist1 not contained in colorlist2: {result}")

