from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random
import os

os.path.dirname(os.getcwd())

# 随机字母
def random_char():
	return chr(random.randint(64, 255))

# 随机颜色1
def random_color1():
	return (random.randint(64,255),random.randint(64,255), random.randint(64,255))

# 随机颜色2
def random_color2():
	return (random.randint(32,127), random.randint(32,127), random.randint(32,127))

# 图片的宽高
width = 60 * 4
height = 60

# 创建新的图片对象
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象
font = ImageFont.truetype('../1.ttf', 36)

# 创建Draw对象, 画笔
draw = ImageDraw.Draw(image)

# 填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=random_color1())

# 输出文字
for t in range(4):
	draw.text((60 * t + 10, 15), random_char(), font=font, fill=random_color2())

# 模糊
# image = image.filter(ImageFilter.BLUR)
image.save('../images/code.jpg', 'jpeg')