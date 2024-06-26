import datetime
import json
import os

from PIL import Image, ImageDraw, ImageFont

from get_gradient_background import get_gradient_background
from get_screen_resolution import get_screen_resolution
from set_wallpaper import set_wallpaper

# Init constants
SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_resolution()
PATH = os.path.expanduser('~/wallpaper.png')
FONT_SIZE = 36

if __name__ == "__main__":
    # Get json file.
    with open(os.getenv('TASK_PATH') + '/sample.json') as f:
        tasks = json.load(f)

    # Create image.
    img = get_gradient_background(SCREEN_WIDTH, SCREEN_HEIGHT)
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('Consolas.ttf', FONT_SIZE)
    y_count = 0

    # Add date.
    now = datetime.datetime.now()
    text = f'Updated on {now.strftime("%Y-%m-%d %H:%M:%S")}.'
    text_width = fnt.getlength(text)
    text_height = FONT_SIZE
    x = (SCREEN_WIDTH - text_width) / 2
    d.text(
        (x, text_height * y_count),
        text,
        font=fnt,
        fill=(255, 242, 176)
    )
    y_count += 2

    # Add text.
    tasks.sort(key=lambda x: x['task'])
    for task in tasks:
        text = ""
        text += f"{task['task']} [{task['progress']}%]"
        text += (f", {task['ddl']}" if 'ddl' in task else "")
        text_width = fnt.getlength(text)
        text_height = FONT_SIZE
        x = (SCREEN_WIDTH - text_width) / 2
        y = text_height * y_count
        y_count += 1
        d.text(
            (x, y),
            text,
            font=fnt,
            fill=(255, 242, 176)
        )

    # Save image.
    img.save(PATH)
    print(PATH)

    # Set wallpaper for Windows.
    set_wallpaper(PATH)

