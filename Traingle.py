def calculate_area_base_height(base, height):
    """Calculates the area of a triangle given its base and height."""
    return 0.5 * base * height

# Example usage:
base_val = float(input("Enter the base of the triangle: "))
height_val = float(input("Enter the height of the triangle: "))

area = calculate_area_base_height(base_val, height_val)
print(f"The area of the triangle is: {area}")
