import random

"""
Defines a Point class to represent and compare 2D coordinates based on their distance from the origin.
"""

class Point:  # Class name follows PascalCase convention
    def __init__(self, x, y):  # Initializes an instance of Point; called automatically
        # self refers to the current instance of the class
        # __init__ is a special method (dunder method)
        """
        Initialize a Point object with specified x and y coordinates.

        :param x: X-coordinate
        :param y: Y-coordinate
        """
        self.x = x  # Store the x value as an instance attribute
        self.y = y  # Store the y value as an instance attribute

    def __str__(self):
        """
        Defines the string representation used when printing the object.

        :return: Formatted string '<x=val, y=val>'
        """
        return f"<x={self.x}, y={self.y}>"

    def __repr__(self):  # Used for displaying the object in the console
        """
        Defines the official string representation of the object.

        :return: Same formatted output as __str__
        """
        return self.__str__()  # Delegates to __str__ for consistency

    def distance_to_orig(self):
        """
        Computes the Euclidean distance of the point from the origin (0, 0).

        :return: Distance calculated using the formula sqrt(x^2 + y^2)
        """
        return (self.x**2 + self.y**2)**0.5  # Apply the distance formula

    def __gt__(self, other):  # Greater-than comparison between points
        """
        Compares two points based on their distance from the origin.

        :param other: Another Point object to compare with
        :return: True if self is farther from origin than other
        """
        my_distance = self.distance_to_orig()
        other_distance = other.distance_to_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        """
        Checks if two points are equidistant from the origin.

        :param other: Another Point object to compare with
        :return: True if both are equally distant from the origin
        """
        my_distance = self.distance_to_orig()
        other_distance = other.distance_to_orig()
        return my_distance == other_distance

if __name__ == "__main__":  # Ensures code only runs when executed directly
    # Instantiate Point objects
    p = Point(1, 2)  # Instance with coordinates (1, 2)
    p2 = Point(2, 3)
    p4 = Point(1, -55)

    # Access and print attributes
    print(f"p.x={p.x} & p.y={p.y}")
    print(f"p4.x={p.x} & p4.y={p.y}")

    p.x = 20  # Modify x value of the point
    print(f"p.x={p.x} & p.y={p.y}")

    print(p)  # Display point using __str__

    # Generate a list of 5 random Point objects
    points = []
    for i in range(5):
        points.append(Point(random.randint(-10, 10),  # Random x-coordinate
                            random.randint(-10, 10)))  # Random y-coordinate

    print("I got these 5 random points:")
    for p in points:
        print(p)

    print(points)  # List uses __repr__ to display objects

    # Demonstrate distance calculation and comparison
    p = Point(3, 4)
    print(p.distance_to_orig())  # Expected output: 5

    p2 = Point(1, 1)
    print(f"I am checking p > p2: {p > p2}")  # Should return True
    print(f"I am checking p == p2: {p == p2}")  # Should return False

    # Sort the list of points based on distance from origin
    print(f"The sorted list of points is:")
    points.sort()  # Sorting relies on __gt__ and __eq__
    print(points)
