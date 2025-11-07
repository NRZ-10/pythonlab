class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        total_seconds = self.second + other.second
        extra_minute = total_seconds // 60
        seconds = total_seconds % 60

        total_minutes = self.minute + other.minute + extra_minute
        extra_hour = total_minutes // 60
        minutes = total_minutes % 60

        total_hours = self.hour + other.hour + extra_hour
        hours = total_hours % 24  # 24-hour format

        return Time(hours, minutes, seconds)

    def display(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")


print("Enter first time:")
h1 = int(input("Hour: "))
m1 = int(input("Minute: "))
s1 = int(input("Second: "))

print("\nEnter second time:")
h2 = int(input("Hour: "))
m2 = int(input("Minute: "))
s2 = int(input("Second: "))

t1 = Time(h1, m1, s1)
t2 = Time(h2, m2, s2)

t3 = t1 + t2

print("\nSum of times:")
t3.display()

