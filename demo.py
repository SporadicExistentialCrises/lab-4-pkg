from geometry.shapes import Circle, Square, Shape
from geometry.utils import area_stats

my_circle = Circle(5)
my_square = Square(4)
print(f"Circle area: {my_circle.area()}")
print(f"Square area: {my_square.area()}")
print("Area statistics:", area_stats(my_circle, my_square))