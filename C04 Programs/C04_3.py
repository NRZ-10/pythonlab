class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __lt__(self, other):
        return self.area() < other.area()

l1 = float(input("Enter length of first rectangle: "))
w1 = float(input("Enter width of first rectangle: "))
rect1 = Rectangle(l1,w1)


l2 = float(input("Enter length of second rectangle: "))
w2 = float(input("Enter width of second rectangle: "))
rect2 = Rectangle(l2,w2)

if rect1 < rect2:
    print("First rectangle is smaller than second rectangle.")
else:
     print("First rectangle is greater than second rectangle.")

