#!/usr/bin/env python3
#-*-coding: utf-8-*-

import random

#xxxxx-xxxxx-xxxxx-xxxxx-xxxxx
#python3 chr()默认支持unicode
def ranChar():
    i = random.randint(0, 2)
    if i == 0:
        return random.randint(65, 90)
    elif i == 1:
        return random.randint(97, 122)
    else:
        return random.randint(48, 57)
    
def generateActivition():
    str = ''
    for i in range(5):
        for j in range(5):
            str += chr(ranChar())
        if i < 4:
            str += '-'
    return str

print(generateActivition())
