# main.py

from polymorphism_demo import Shape, Rectangle, Circle
# No need to import math here, as it's used within polymorphism_demo.py already.

def main():
    # Create a list containing different types of shapes.
    shapes = [
        Rectangle(10, 5), # A Rectangle object
        Circle(7)         # A Circle object
    ]

    # Loop through each shape in the list.
    for shape in shapes:
        # Polymorphism in action: calling .area() on different shape types!
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()