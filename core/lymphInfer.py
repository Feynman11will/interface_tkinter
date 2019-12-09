'''
@Author: your name
@Date: 2019-12-09 16:22:44
@LastEditTime: 2019-12-09 19:35:50
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /05github/interface_tkinter/core/lymphInfer.py
'''
import torch
import numpy as np 
import os 
import sys
import cv2
na = os.path.realpath(__file__)
pna = os.path.dirname(na)
ppna = os.path.dirname(pna)
sys.path.append(ppna)

from lib.PyMIC.pymic.train_infer.train_infer import Infer

def inferSingleImg(image):
    state = 'IOInfer'
    image = np.asarray(image,np.float)
    
    image = np.resize(image, (64,64))
    image = image[None,None,:,:]
    cfg_file = '/Users/deepwise/Documents/05github/interface_tkinter/lib/PyMIC/examples/lymph/config/train_test.cfg'
    return Infer(image, stage = state,cfg_file = cfg_file)
    


if __name__ == "__main__":
    # state = 'test'
    # cfg_file = '/Users/deepwise/Documents/05github/PyMIC/examples/lymph/config/train_test.cfg'
    # Infer(stage = "test",cfg_file = cfg_file)
    pass