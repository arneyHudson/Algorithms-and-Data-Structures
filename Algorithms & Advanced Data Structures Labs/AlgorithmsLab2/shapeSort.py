import numpy as np
import matplotlib.pyplot as plt


def is_convex(points):
    def cross_product(p1, p2, p3):
        # Calculate the cross product of vectors (p2-p1) and (p3-p2)
        return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])

    n = len(points)

    if n < 3:
        return False  # Not enough points to form a polygon

    # Initialize the sign of the first cross product
    sign = 0

    for i in range(n):
        # Get three consecutive points
        p1, p2, p3 = points[i], points[(i + 1) % n], points[(i + 2) % n]

        # Calculate the cross product
        current_cross_product = cross_product(p1, p2, p3)

        # If this is the first cross product, set the sign
        if sign == 0:
            sign = current_cross_product
        else:
            # If the sign of the current cross product is different from the previous one, it's not convex
            if sign * current_cross_product < 0:
                return False

    # If we haven't returned False, the polygon is convex
    return True


def generate_random_convex_shape(n):
    angles = np.linspace(0, 2 * np.pi, n)
    radii = np.random.uniform(0.5, 1.5, n)  # Random radii
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    return list(zip(x, y))


# Function to generate a random concave shape with 'n' points
def generate_random_concave_shape(n):
    # Randomly create points within a bounding box
    x = np.random.uniform(-2, 2, n)
    y = np.random.uniform(-2, 2, n)

    # Modify some points to create concavity
    for i in range(n // 5, 2 * n // 5):
        x[i] += 1
        y[i] += 1

    return list(zip(x, y))

def create_random_shapes():
    # Generate a random convex shape with 100 points
    convex_shape = generate_random_convex_shape(100)

    # Generate a random concave shape with 100 points
    concave_shape = generate_random_concave_shape(100)

    # Plot the shapes
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.plot(*zip(*convex_shape), 'o-')
    plt.title("Convex Shape")

    plt.subplot(1, 2, 2)
    plt.plot(*zip(*concave_shape), 'o-')
    plt.title("Concave Shape")

    plt.tight_layout()
    plt.show()