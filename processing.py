import Tkinter as tk
import tkFileDialog as filedialog
import numpy as np
import cv2
import cv2.cv as cv
import time
import matplotlib.pyplot as plt

def setLabel(cleanLabels,sensorLow,sensorHigh):
    div=(sensorHigh-sensorLow)/4
    finalLabels=np.zeros((0,4),'float')
    for label in cleanLabels:
        if sensorLow<=label<sensorLow+div:
            a=[1,-1,-1,-1]
        if sensorLow+div<=label<sensorLow+(2*div):
            a=[-1,1,-1,-1]
        if sensorLow+(2*div)<=label<sensorHigh-div:
            a=[-1,-1,1,-1]
        if sensorHigh-div<=label<=sensorHigh:
            a=[-1,-1,-1,1]
        temp=np.vstack((finalLabels,a))
        finalLabels=temp
    return finalLabels

def setSensorLimits():
    l=raw_input("Enter lower threshold value of sensor:")
    h=raw_input("Enter higher threshold value of sensor:")
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
        ret, frame = cam.read()
        if ret==True:
            frame2=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            gray=cv2.resize(frame2,None,fx=0.5,fy=0.5)
            if (labels[i]<sensorLow)|(labels[i]>sensorHigh):
                continue
            temp=np.vstack((cleanLabels,labels[i]))
            a=np.reshape(gray,(1,size))
            temp2=np.vstack((cleanFeatures,a))
            count=count+1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
        cleanLabels=temp
        cleanFeatures=temp2
    print cleanLabels.shape
    plot(cleanLabels)
    cam.release()
    cv2.destroyAllWindows()
    return count,cleanLabels,cleanFeatures

def saveFeatures(features):
    fileName=raw_input("Enter the filename to save features to(no ext. reqd):")
    np.savez(fileName,features)

def saveLabels(labels):
    fileName=raw_input("Enter the filename to save labels to(no ext. reqd):")
    np.savez(fileName,labels)

def plot(labels):
    l=len(labels)
    t=np.arange(0.0,l,1)
    plt.plot(t,labels)
    plt.show()
    name=raw_input("Enter name to store plot(with .png):")
    plt.savefig(name)


labelPath=chooseLabelPath()
featurePath=chooseFeaturePath()
total,cleanLabels,cleanFeatures=cleanVideo(labelPath,featurePath,320,240)
sensorLow,sensorHigh=setSensorLimits()
finalLabels=setLabel(cleanLabels,sensorLow,sensorHigh)
saveFeatures(cleanFeatures)
saveLabels(finalLabels)
