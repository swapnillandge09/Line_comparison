# line_comparison.py
print("Welcome to Line Comparison Computation Program on Master Branch")

import math

def calculate_length(point1, point2):
    """Calculate the length of a line segment given two points."""
    x1, y1 = point1
    x2, y2 = point2
    length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return length

def main():
    # Input points
    x1 = float(input("Enter x1 coordinate: "))
    y1 = float(input("Enter y1 coordinate: "))
    x2 = float(input("Enter x2 coordinate: "))
    y2 = float(input("Enter y2 coordinate: "))

    # Define points
    point1 = (x1, y1)
    point2 = (x2, y2)

    # Calculate length
    length = calculate_length(point1, point2)
    print(f"The length of the line segment between {point1} and {point2} is: {length}")

if __name__ == "__main__":
    main()
