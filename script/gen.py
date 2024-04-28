from PIL import Image, ImageDraw, ImageFont
import json

# 读取JSON数据
with open('progress.json') as f:
    tasks = json.load(f)

# 创建图像
img = Image.new('RGB', (800, 600), color = (255, 255, 255))
d = ImageDraw.Draw(img)
fnt = ImageFont.load_default()

# 绘制进度条
y = 50
for task in tasks:
    d.text((10,y), f"{task['task']} [{task['progress']}%]", font=fnt, fill=(0, 0, 0))
    d.rectangle([10, y + 20, task['progress']*7.8 + 10, y + 40], fill=(0, 128, 0))
    y += 60

# 保存图片
img.save('progress.png')
