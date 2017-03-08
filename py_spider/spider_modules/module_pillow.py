# -*- coding: utf-8 -*-
# @Date:   2016-07-12 13:06:08
# @Last Modified time: 2017-03-08 19:55:25
"""
PIL、pillow同义
pip install pillow
"""
import os
from PIL import Image

im = Image.open(os.path.join(os.path.dirname(
    __file__), 'test.jpg'))  # 打开一个jpg图像文件


def change_size(image, mult_w, mult_h):
    '''
    图像缩放
    获得图像尺寸，缩放到50%，保存为jpeg格式
    '''
    w, h = image.size
    image.thumbnail((w // 2, h // 2))
    image.save(os.path.join(os.path.dirname(
        __file__), 'thumbnail.jpg'), 'jpeg')
'''
模糊效果
'''
from PIL import ImageFilter
im = Image.open(os.path.join(os.path.dirname(
    __file__), 'test.jpg'))
im2 = im.filter(ImageFilter.BLUR)
im2.save(os.path.join(os.path.dirname(__file__), 'blur.jpg'), 'jpeg')
'''
PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片
'''
from PIL import ImageDraw, ImageFont
import random

# 随机字母:


def rndChar():
    return chr(random.randint(65, 90))
rndChar = rndChar()
print rndChar

# 随机颜色1:


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
rndColor = rndColor()
print rndColor

# 随机颜色2:


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
rndColor2 = rndColor2()
print rndColor2


# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)

# 创建Draw对象:
draw = ImageDraw.Draw(image)

# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save(os.path.join(os.path.abspath('..'), 'code.jpg'), 'jpeg')
