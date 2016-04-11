#!/usr/bin/env python3
#-*-coding: utf-8-*-

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

font_size = 20

#设置字体
font = ImageFont.truetype('arial.ttf', font_size)

#载入图片
imagefile = "test.png"
image = Image.open(imagefile)
w, h = image.size

#添加文字，并保存
draw = ImageDraw.Draw(image)
draw.text((w-font_size-5, 5), '4', (255, 0, 0), font=font)

image.save("final.png")
print('successful!')
