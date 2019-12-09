'''
@Author: your name
@Date: 2019-12-09 13:37:35
@LastEditTime: 2019-12-09 19:43:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /05github/interface_tkinter/core/drawer.py
'''
import tkinter as tk # this is in python 3.4. For python 2.x import Tkinter
from PIL import Image, ImageTk
from getConfig import parse_config
import numpy as np
from lymphInfer import inferSingleImg

def getPatchImg(coord,image):
    
    [x1,y1, x2,y2] = coord
    resImage = image[y1:y2,x1:x2,:]
    print(f"image.shape----->>:{image.shape}")
    return resImage



    
def readNpyImg(imgPath):
    image= None
    if imgPath.endswith('.npy'):
        image = np.load(imgPath)
    return image


class ExampleApp(tk.Tk):
    def __init__(self,imagePath):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.canvas = tk.Canvas(self, width=512, height=512, cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.rect = None

        self.start_x = None
        self.start_y = None

        self.imagePath = imagePath
        npImage = readNpyImg('/Users/deepwise/Documents/05github/interface_tkinter/resoure/image_0.npy')
        self.draw_image_fromNumpy(npImage,PosX=0,PosY=0)
        npImage2 = readNpyImg('/Users/deepwise/Documents/05github/interface_tkinter/resoure/mask_0.npy')
        npImage2 = npImage2*255
        self.draw_image_fromNumpy2(npImage2,PosX=520,PosY=0)

    def drawImage(self,imgPath):
        if imgPath.endswith('.npy'):
            self.im = readNpyImg(imgPath)
        else :
            self.im = Image.open(imgPath)
        self.tk_im = ImageTk.PhotoImage(self.im)
        self.canvas.create_image(0,0,anchor="nw",image=self.tk_im)

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = event.x
        self.start_y = event.y

        # create rectangle if not yet exist
        #if not self.rect:
        self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1)

    def on_move_press(self, event):
        self.endX, self.endY = (event.x, event.y)
        # expand rectangle as you drag the mouse
        self.canvas.coords(self.rect, self.start_x, self.start_y, self.endX, self.endY)

    def on_button_release(self, event):
        coordList=  [self.start_x, self.start_y, self.endX, self.endY]
        print(coordList)

        self.inferImg(coordList)
    def draw_image_fromNumpy(self,npImage,PosX=0,PosY=0):
        img=Image.fromarray(npImage)
        self.imgTk=ImageTk.PhotoImage(img)
        self.canvas.create_image(PosX,PosY,anchor="nw",image=self.imgTk)
    def draw_image_fromNumpy2(self,npImage,PosX=0,PosY=0):
        img=Image.fromarray(npImage)
        self.imgTk2=ImageTk.PhotoImage(img)
        self.canvas.create_image(PosX,PosY,anchor="nw",image=self.imgTk2)
    def draw_image_fromNumpy3(self,npImage,PosX=0,PosY=0):
        img=Image.fromarray(npImage)
        self.imgTk3=ImageTk.PhotoImage(img)
        self.canvas.create_image(PosX,PosY,anchor="nw",image=self.imgTk3)

    def inferImg(self,coordList):
        image= Image.open(self.imagePath)
        w,h= image.size
        npImage = np.array(image)
        
        inferInput = getPatchImg(coordList,npImage)
        inferOut = inferSingleImg(inferInput)
        print(type(inferOut))
        inferOut = inferOut*255.
        print(inferOut[inferOut!=0])
        self.draw_image_fromNumpy3(inferOut*255,PosX=512,PosY=512)
        
        
if __name__ == "__main__":
    
    configPath = '/Users/deepwise/Documents/05github/interface_tkinter/config/config.cfg'
    config = parse_config(configPath)
    print(config)
    app = ExampleApp(config['image']['sourceimg'])
    app.mainloop()