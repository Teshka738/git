class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

circle1 = Circle(10)
print("Исходный радиус:", circle1.get_radius())

circle1.set_radius(12)
print("Новый радиус:", circle1.get_radius())