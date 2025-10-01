import math

# Get radius and height from the user
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate the total surface area
total_surface_area = (2 * math.pi * radius**2) + (2 * math.pi * radius * height)

# Display the result
print(f"The total surface area of the cylinder is: {total_surface_area:.2f}")
