#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
from PIL import Image

SuffixImage = ['png', 'jpg', 'jpeg', 'bmp']
width = 800
height = 600

#第一步:遍历目录
def TraversalFolder(filePath):
        folders = os.listdir(filePath)
        for file in folders:
                file = os.path.join(filePath, file)
                if os.path.isdir(file) is True:
                        TraversalFolder(file)
                else:
                        print(file)
                        suffixPos = file[-5:].find('.')
                        if suffixPos != -1:
                                suffixName = file[-4+suffixPos:]
                        else:
                                continue
                        if suffixName not in SuffixImage:
                                continue
                        #打开文件，修改分辨率
                        im = Image.open(file)
                        w, h = im.size
                        p = max(w/width, h/height)
                        print(p)
                        imChange = im.resize((int(w/p), int(h/p)), Image.ANTIALIAS)
                        imChange.save(file)

def TraversalFolderOS(filePath):
        for fpath, dirs, fs in os.walk(filePath):
                for f in fs:
                        print(os.path.join(fpath, f))

if __name__ == '__main__':
	startTime = time.time()
	TraversalFolder(r'C:\Users\dc\Desktop\mail')
	endTime = time.time()
	print('用时: %ds', endTime-startTime)
##	TraversalFolderOS(r'C:\Users\dc\Desktop\mail')

	
	
		
	
            
	
