from point import Point
import random

class ColorPoint(Point):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint(1,2,"red")
print(p)
colors = ["red", "green", "blue", "yellow", "black", "magenta",
          "cyan", "white", "burgundy", "periwinkle", "marsala"]
color_points = []
for i in range(10):
    color_points.append(
        ColorPoint(random.randint(-10, 10),
                   random.randint(-10, 10),
                   random.choice(colors)))

print(color_points)
color_points.sort()
print(color_points)