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

    def __init__(self,videopath,labelpath):
        cam=cv2.VideoCapture(videopath)
        labels=np.loadtxt(labelpath,delimiter=',')
        print "Initialization successful"

    def clean(self):
        i=0
        while (cam.isOpened()):
            ret, frame = cam.read()
            cv2.imshow('frame',frame
