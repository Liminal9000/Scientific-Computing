import math

# Function to calculate the area of different shapes
def calculate_area(shape, dimension1, dimension2=0):
    if shape == "circle":
        return math.pi * (dimension1 ** 2)
    elif shape == "rectangle":
        return dimension1 * dimension2
    elif shape == "triangle":
        return 0.5 * dimension1 * dimension2
    else:
        return "Invalid shape"

# Test the function with different shapes
circle_area = calculate_area("circle", 5)
rectangle_area = calculate_area("rectangle", 4, 6)
triangle_area = calculate_area("triangle", 3, 7)

print(f"Area of the circle: {circle_area:.2f}")
print(f"Area of the rectangle: {rectangle_area:.2f}")
print(f"Area of the triangle: {triangle_area:.2f}")
