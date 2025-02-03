from utils.angle_calculator import calculate_angle
print("Angle calculator imported successfully")

# Test the function
test_points = [
    [0, 0],  # Point a
    [1, 1],  # Point b
    [2, 0]   # Point c
]
angle = calculate_angle(test_points[0], test_points[1], test_points[2])
print(f"Test angle calculated: {angle}")