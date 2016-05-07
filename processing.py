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

def convertFeature(cleanVideoPath):
    print cleanVideoPath
    cam = cv2.VideoCapture(cleanVideoPath)
    final=np.zeros((1,0),'float')
    a=np.zeros((1,0),'float')
    while(cam.isOpened()):
        ret,frame=cam.read()
        cv2.imshow('frame',frame)
        if ret==True:
            temp=np.reshape(frame,(1,len(frame)*len(frame[0])))
            print temp.shape
            a=np.vstack(final,temp)
            final=a
    print final.shape
    cam.release()
    final=final+0.0
    return final

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
            #cv2.imshow('frame',gray)
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

sensorLow,sensorHigh=setSensorLimits()
labelPath=chooseLabelPath()
featurePath=chooseFeaturePath()
total,cleanLabels,cleanVideoPath=cleanVideo(labelPath,featurePath)
cleanFeatures=convertFeature(cleanVideoPath)
