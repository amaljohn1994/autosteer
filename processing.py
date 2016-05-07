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

def cleanVideo(labelPath,featurePath,hor,ver):
    labels=np.zeros((0,1),'float')
    size=hor*ver
    cleanLabels=np.zeros((0,1),'float')
    cleanFeatures=np.zeros((0,size),'float')
    cam = cv2.VideoCapture(featurePath)
    labels=np.loadtxt(labelPath,delimiter=',')
    i=-1
    count=0
    while(cam.isOpened()):
        i=i+1
        print i
        ret, frame = cam.read()
        if ret==True:
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            if (labels[i]<sensorLow)|(labels[i]>sensorHigh):
                continue
            temp=np.vstack((cleanLabels,labels[i]))
            a=np.reshape(gray,(1,size))
            temp2=np.vstack((cleanFeatures,a))
            print cleanLabels.shape
            count=count+1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
        cleanLabels=temp
        cleanFeatures=temp2
    cam.release()
    cv2.destroyAllWindows()
    print cleanFeatures.shape
    print cleanLabels.shape
    return count,cleanLabels,cleanFeatures

sensorLow,sensorHigh=setSensorLimits()
labelPath=chooseLabelPath()
featurePath=chooseFeaturePath()
total,cleanLabels,cleanFeatures=cleanVideo(labelPath,featurePath,640,480)
