import Tkinter as tk
import tkFileDialog as filedialog
import numpy as np
import cv2
from time import sleep
import time

class clean_samples:
    videopath=''
    labelpath=''
    sensorlow=0
    sensorhigh=0

    def __init__(self):
        sensorhigh=raw_input("Higher Threshold of sensor value:")
        sensorlow=raw_input("Lower Threshold of sensor value")
        root=tk.Tk()
        root.withdraw()
        print "Select video path"
        videopath=filedialog.askopenfilename()
        root=tk.Tk()
        root.withdraw()
        print "Select feature path"
        labelpath=filedialog.askopenfilename()

    
