#!/usr/bin/env python3
#-*-coding: utf-8-*-

from PIL import Image, ImageFilter

def watermark(img_source, img_water, img_des, offset_x, offset_y):
    try:
        im = Image.open(img_source)
        wm = Image.open(img_water)

        layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
        layer.paste(wm, (im.size[0] - offset_x, im.size[1] - offset_y))
        newIm = Image.composite(layer, im, layer)
        newIm.save(img_des)
##        newIm.show()
        print('successful')
        return True
    except Exception as e:
        print('>>>>>>>>>>> WaterMark EXCEPTION: ' + str(e))
        return False

def main():
    watermark('原始图片.png', '水印图片.png', '最终图片.jpg', 300, 100)

if __name__ == '__main__':
    main()
