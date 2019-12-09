'''
@Author: your name
@Date: 2019-12-09 13:46:11
@LastEditTime: 2019-12-09 13:49:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /05github/interface_tkinter/bin/draw.py
'''

import os
import sys
na = os.path.realpath(__file__)
pna = os.path.dirname(na)
ppna = os.path.dirname(pna)
sys.path.append(ppna)


from core.drawer import ExampleApp



if __name__=="__main__":
    app =ExampleApp()
    app.mainloop()