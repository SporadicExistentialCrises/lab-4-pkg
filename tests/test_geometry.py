import pytest
from geometry import Square, Circle, area_stats
from geometry.shapes import Shape

def test_square_area():
    # basic test
    square = Square(4)
    assert square.area() == 16
    # zero side length
    square = Square(0)
    assert square.area() == 0
    # floating point side length
    square = Square(2.5)
    assert square.area() == pytest.approx(6.25, rel=1e-4)
    # negative side length should raise ValueError
    square = Square(-3)
    with pytest.raises(ValueError):
        square.area()
    # non-numeric side length should raise TypeError
    square = Square("a")
    with pytest.raises(TypeError):
        square.area()

def test_circle_area():
    #basic test
    circle = Circle(3)
    assert circle.area() == pytest.approx(28.2743, rel=1e-4)
    # zero radius
    circle = Circle(0)
    assert circle.area() == 0
    # floating point radius
    circle = Circle(1.5)
    assert circle.area() == pytest.approx(7.0686, rel=1e-4)
    # negative radius should raise ValueError
    circle = Circle(-2)
    with pytest.raises(ValueError):
        circle.area()
    # non-numeric radius should raise TypeError
    circle = Circle("b")
    with pytest.raises(TypeError):
        circle.area()

def test_area_stats():
    # make sure returns a dict
    assert type(area_stats(Square(3))) == dict
    # size of dictionary is 5
    assert len(area_stats(Square(3))) == 5
    # raises valueError if no shapes provided
    with pytest.raises(ValueError):
        area_stats()