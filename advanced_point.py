from color_point import ColorPoint, PointException

"""
Extends ColorPoint by adding advanced features like controlled color values, property accessors,
class methods for color list updates, and static methods for point construction and distance calculation.
"""

class AdvancedPoint(ColorPoint):
    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]

    def __init__(self, x, y, color):
        # Raise error if color is not in allowed list
        if color not in self.COLORS:
            raise TypeError(f"Invalid color, must be one of the {self.COLORS}")

        self._x = x  # Internal storage for x-coordinate
        self._y = y  # Internal storage for y-coordinate
        self._color = color  # Internal storage for color

    @property
    def x(self):
        """Getter for x-coordinate."""
        return self._x

    @x.setter
    def x(self, value):
        """Setter for x-coordinate."""
        self._x = value

    @property
    def y(self):
        """Getter for y-coordinate."""
        return self._y

    @property
    def color(self):
        """Getter for color."""
        return self._color

    @classmethod
    def add_color(cls, color):
        """
        Adds a new valid color to the class-level COLORS list.

        Args:
            color (str): The color to add
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color="red"):
        """
        Creates an AdvancedPoint from a coordinate tuple.

        Args:
            coordinate (tuple): A tuple containing (x, y)
            color (str): Color to assign, default is 'red'

        Returns:
            AdvancedPoint: A new instance with the given values
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Computes the Euclidean distance between two AdvancedPoint instances.

        Args:
            p1 (AdvancedPoint): First point
            p2 (AdvancedPoint): Second point

        Returns:
            float: Euclidean distance between p1 and p2
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        """
        Computes distance from this point to another point.

        Args:
            p (AdvancedPoint): The other point

        Returns:
            float: Euclidean distance to the other point
        """
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

# Example usage
AdvancedPoint.add_color("rojo")  # Add a new allowed color
p = AdvancedPoint(1, 2, "rojo")
print(p.x)  # Access x-coordinate using getter
print(p)  # Uses inherited __str__ from ColorPoint
print(p.distance_orig())  # Inherited from Point

p2 = AdvancedPoint.from_tuple((3, 2))  # Create from tuple
print(p2)
print(AdvancedPoint.distance_2_points(p, p2))  # Static method call
print(p.distance_to_other(p2))  # Instance method call