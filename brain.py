import Tkinter as tk
import tkFileDialog as filedialog
import numpy as np
import cv2
import cv2.cv as cv
import time

def setSensorLimits():
    l=raw_input("Enter lower threshold value of sensor")
    h=raw_input("Enter higher threshold value of sensor")
    return float(l),float(h)

def chooseFeaturePath():
    print "Select path for features"
    root=tk.Tk()
    root.withdraw()
    a=filedialog.askopenfilename()
    return a


def chooseLabelPath():
    print "Select path for labels"
    root=tk.Tk()
    root.withdraw()
    a=filedialog.askopenfilename()
    return a


def cleanVideo(labelPath,featurePath):
    labels=np.zeros((0,1),'float')
    cleanLabels=np.zeros((0,1),'float')
    cam = cv2.VideoCapture(featurePath)
    labels=np.loadtxt(labelPath,delimiter=',')
    i=-1
    count=0
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    out = cv2.VideoWriter('cleanedVideo.avi',fourcc, 20.0, (640,480))
    while(cam.isOpened()):
        i=i+1
        ret, frame = cam.read()
        if ret==True:
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame',gray)
            if (labels[i]<sensorLow)|(labels[i]>sensorHigh):
                continue
            temp=np.vstack((cleanLabels,labels[i]))
            count=count+1
            out.write(gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
        cleanLabels=temp
    # Release everything if job is finished
    cam.release()
    out.release()
    cv2.destroyAllWindows()
    return count,cleanLabels,"cleanVideo.avi"

def setNetParams():
    t=int(raw_input("Total number of layers for network:"))
    netParams=np.zeros((1,t),'int32')
    for i in range(0,t):
        c=i+1
        netParams[0,i]=int(raw_input("Enter no. of neurons in layer %d:"%c))
    return netParams[0]


#sensorLow,sensorHigh=setSensorLimits()
#labelPath=chooseLabelPath()
#featurePath=chooseFeaturePath()
#total,cleanLabels,cleanVideoPath=cleanVideo(labelPath,featurePath)
netParams=etNetParams()
