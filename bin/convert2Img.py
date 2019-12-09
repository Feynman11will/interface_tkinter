'''
@Author: your name
@Date: 2019-12-09 14:42:33
@LastEditTime: 2019-12-09 14:49:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /05github/interface_tkinter/bin/convert2Img.py
'''
import numpy as np 
import os 
def getNpyList(npyPaths):
    if os.path.isfile(npyPaths):
        npyPaths = os.path.dirname(npyPaths)
    npyPathsList = os.listdir(npyPaths)
    fulllNpyNameList = [os.path.join(npyPaths,npyPath) for npyPath in npyPathsList]
    return fulllNpyNameList
def convert2Png(path):
    getNpyList
