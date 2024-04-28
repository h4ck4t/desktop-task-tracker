import math

from PIL import Image, ImageDraw

def get_gradient_background(width, height, center_color = (51, 0, 51), outer_color = (0, 0, 0)):
    # Create a new image with RGB mode
    img = Image.new('RGB', (width, height))
    d = ImageDraw.Draw(img)

    # Calculate the center point
    center_x, center_y = width // 2, height // 2
    max_distance = math.sqrt(center_x**2 + center_y**2)

    # Draw the gradient
    for x in range(width):
        for y in range(height):
            # Calculate distance to center
            distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            ratio = distance / max_distance

            # Calculate intermediate color
            r = int(center_color[0] * (1 - ratio) + outer_color[0] * ratio)
            g = int(center_color[1] * (1 - ratio) + outer_color[1] * ratio)
            b = int(center_color[2] * (1 - ratio) + outer_color[2] * ratio)

            # Set pixel color
            d.point((x, y), (r, g, b))

    return img
