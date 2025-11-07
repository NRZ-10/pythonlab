class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

r1 = Rectangle(float(input("Enter length of first rectangle: ")),
               float(input("Enter breadth of first rectangle: ")))

r2 = Rectangle(float(input("Enter length of second rectangle: ")),
               float(input("Enter breadth of second rectangle: ")))

print("\nRectangle 1-Area: ",r1.area(),"Perimeter: ",r1.perimeter())
print("\nRectangle 2-Area: ",r2.area(),"Perimeter: ",r2.perimeter())

if r1.area() > r2.area():
    print("\nRectangle 1 is larger than Rectangle 2.")
elif r1.area() < r2.area():
    print("\nRectangle 2 is larger than Rectangle 1.")
else:
    print("\nRectangle 1 and 2 have the  same area.")

