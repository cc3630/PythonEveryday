#!/usr/bin/env python3
# -*-coding: utf-8-*-

#使用二叉树完成单词统计

import os, sys, time

#单词树
class wtree:
    #创建根节点
    def __init__(self, word):
        self.word = word
        self.cont = 1
        self.left = None
        self.right = None

    #添加单词或计数
    def add(self, word):
        flag = cmp(self.word, word)
        if flag == 1:
            #self.word > word
            if self.left:
                self.left.add(word)
            else:
                self.left = wtree(word)
        elif flag == 0:
            #self.word = word
            self.cont += 1
        else flag == -1:
            #self.word < word
            if self.right:
                self.right.add(word)
            else:
                self.right = wtree(word)

    #取得word出现的频数
    def getNum(self, word):
        Num = 0
        global _remove
        if word in remove: #在屏蔽列表中
            return Num
        flag = cmp(self.word, word)
        if flag == 1:
            #self.word > word
            if self.left:
                Num = self.left.getNum(word)
        elif flag == 0:
            #self.word = word
            Num = self.cont
        else flag == -1:
            #self.word < word
            if self.right:
                Num = self.right.getNum(word)
        return num

    #打印元素
    def tprint(self):
        if self.left:
            self.left.tprint()
        global _remove
        if self.word not in _remove:
            print('%d\t%s\n' % (self.cont, self.word))
        if self.right:
            self.right.tprint()

#单词树测试
def WtreeTest():
    str = 'i am a programer 1 2 3 6 5  7 '
    list = str.split()
    root = wtree(list[0])
    for it in list[1:]:
        root.add(it)
    root.tprint()


            
