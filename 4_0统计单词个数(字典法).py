#!/usr/bin/env python3
# -*-coding: utf-8-*-

#使用内置字典完成统计功能

import os, sys, time

def statisticsWords(filename):
    file = open(filename, 'r', encoding='utf-8')
    D = {}
    for line in file:
        for str in line.split():
            if str.isalpha():
                str = str.lower()
                if D:
                    D[str] = D.get(str, 0) + 1
                else:
                    D.update({str:1})

##    for key, num in D.items():
##        print('%s: %d, ' %(key, num), end="")

starttime = time.time()
statisticsWords('test.txt')
endtime = time.time()
print('use time: %s second' % (endtime-starttime))

#use time: 0.07200407981872559 second
