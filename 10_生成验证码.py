#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import string, sys, random
import time

font_path = 'c:\\Windows\\Fonts\\Arial.ttf'
number = 4
size = (100, 30)
bgcolor = (255, 255, 255)
fontcolor = (0, 0, 255)
linecolor = (255, 0, 0)
draw_line = True
line_number = (1, 5)

#生成随机字符串
def GeneText(number):
    return ''.join(random.sample(string.ascii_letters, number))

#绘制干扰线
def GeneLine(draw, width, height):
    begin = (random.randint(0, width), random.randint(0, height))
    end = (random.randint(0, width), random.randint(0, height))
    draw.line([begin, end], fill=linecolor)
    
#生成验证码
def GeneCode():
    width, height = size
    image = Image.new('RGBA', (width, height), bgcolor)
    font = ImageFont.truetype(font_path, 25)
    draw = ImageDraw.Draw(image)
    text = GeneText(number)
    font_width, font_height = font.getsize(text)
    draw.text(((width-font_width)/number, (height-font_height)/number), text,\
              font = font, fill=fontcolor)
    if draw_line:
        GeneLine(draw, width, height)

    #创建扭曲
    image = image.transform((width+20, height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),\
                            Image.BILINEAR)
    #滤镜，边界加强
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    image.save('code.png')

if __name__ == '__main__':
    startTime = time.time()
    GeneCode()
    endTime = time.time()
    print('用时%ds' % (endTime-startTime))
