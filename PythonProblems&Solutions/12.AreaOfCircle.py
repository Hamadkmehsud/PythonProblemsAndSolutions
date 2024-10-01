class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        area_circle = (22/7) * (self.radius**2)
        return area_circle
    @property
    def perimeter(self):
        return 2 * (22/7) * self.radius

a = Circle(4)

print(round(a.area, 2))
print(round(a.perimeter,2))