import Tkinter as tk
import tkFileDialog as filedialog
import numpy as np
import cv2
from time import sleep
import time
cleaned_labels=np.zeros(1,)
labels=np.zeros(1,)
fourcc = cv2.cv.CV_FOURCC(*'XVID')


class clean_samples:
    videopath=''
    labelpath=''
    sensorlow=0
    sensorhigh=0
    no_of_samples=0
    cam=cv2.VideoCapture(str(videopath))

    def __init__(self,vidpath,labpath):
        videopath=vidpath
        labelpath=labpath
        print videopath
        cam=cv2.VideoCapture(str(videopath))
        labels=np.loadtxt(labelpath,delimiter=',')
        sensorlow=raw_input("Enter sensor triggering value:")
        sensorhigh=raw_input("Enter sensor limiting value:")
        no_of_samples=len(labels)
        print "Initialization successful"

    def clean(self):
        i=0
        cam=cv2.VideoCapture(str(videopath))
        out = cv2.VideoWriter('cleaned_video.avi',fourcc, 20.0, (640,480))
        while (cam.isOpened()):
            ret,frame=cam.read()
            cv2.imshow('Processing Video..',frame)
            if labels[i]==0:
                continue
            if (labels[i]>sensorhigh)|(labels[i]<sensorlow):
                continue
            out.write(frame)
