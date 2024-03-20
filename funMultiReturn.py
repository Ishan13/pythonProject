def calculate_rectangle_properties(length, width):
    """Calculate properties of a rectangle given its length and width."""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Call the function and unpack the returned values
rectangle_area, rectangle_perimeter = calculate_rectangle_properties(4, 6)

print("Area of the rectangle:", rectangle_area)
print("Perimeter of the rectangle:", rectangle_perimeter)
