import json
import os

from PIL import Image, ImageDraw, ImageFont

from get_gradient_background import get_gradient_background
from get_screen_resolution import get_screen_resolution
from set_wallpaper import set_wallpaper

# Init constants
SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_resolution()
FILE = 'image.png'
FONT_SIZE = 36

if __name__ == "__main__":
    # Get json file.
    with open(os.getenv('TASK_PATH') + '/sample.json') as f:
        tasks = json.load(f)

    # Create image.
    img = get_gradient_background(SCREEN_WIDTH, SCREEN_HEIGHT)
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('Consolas.ttf', FONT_SIZE)

    # Add text.
    tasks.sort(key=lambda x: x['task'])
    for i, task in enumerate(tasks):
        text = ""
        text += f"{task['task']} [{task['progress']}%]"
        text += (f", {task['ddl']}" if 'ddl' in task else "")
        text_width = fnt.getlength(text)
        text_height = FONT_SIZE
        x = (SCREEN_WIDTH - text_width) / 2
        y = text_height * i
        d.text(
            (x, y),
            text,
            font=fnt,
            fill=(255, 242, 176)
        )

    # Save image.
    img.save(FILE)
    file_path = os.path.abspath(FILE)
    print(file_path)

    # Set wallpaper for Windows.
    set_wallpaper(file_path)

    # Delete image.
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File removed successfully.")
    else:
        print("File does not exist.")

