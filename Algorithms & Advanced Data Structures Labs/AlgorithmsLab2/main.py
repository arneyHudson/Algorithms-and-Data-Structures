# This is a sample Python script.
from shapeSort import is_convex
import numpy as np
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    shapes = {
        "Circle": [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)],
        "Rectangle": [(0, 0), (2, 0), (2, 1), (0, 1)],
        "Star": [(0, 0), (1, 1), (2, 0), (1, 2), (3, 3)],
        "Pentagon": [(0, 0), (1, 0), (1.62, 0.95), (0.62, 1.90), (-0.62, 1.90)]
    }

    for shape_name, shape_points in shapes.items():
        result = is_convex(shape_points)
        if result:
            print(f"{shape_name} is convex")
        else:
            print(f"{shape_name} is not convex")

