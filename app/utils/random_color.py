import random

def random_color():
    # Generate random values for RGB components
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    # Create a hexadecimal color string
    color = "#{:02X}{:02X}{:02X}".format(red, green, blue)

    return color