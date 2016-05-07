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



def setNetParams():
    t=int(raw_input("Total number of layers for network:"))
    netParams=np.zeros((1,t),'int32')
    for i in range(0,t):
        c=i+1
        netParams[0,i]=int(raw_input("Enter no. of neurons in layer %d:"%c))
    return netParams[0]

def setTrainParams():
    moment=float(raw_input("Enter moment scale:"))
    maxIter=int(raw_input("Enter maximum iterations:"))
    maxError=float(raw_input("Enter eror change to stop:"))
    return maxIter,maxError,moment

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

def trainNet(netParams,maxIter,maxError,moment,cleanLabels,cleanFeatures):
    model=cv2.ANN_MLP()
    model.create(netParams)
    criteria = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, maxIter, maxError)
    params = dict(term_crit = criteria,
                   train_method = cv2.ANN_MLP_TRAIN_PARAMS_BACKPROP,
                   bp_dw_scale = moment,
                   bp_moment_scale = 0.0 )
    num_iter=model.train(cleanFeatures,cleanLabels,None,params=params)
    print num_iter

sensorLow,sensorHigh=setSensorLimits()
labelPath=chooseLabelPath()
featurePath=chooseFeaturePath()
total,cleanLabels,cleanVideoPath=cleanVideo(labelPath,featurePath)
netParams=setNetParams()
maxIter,maxError,moment=setTrainParams()
cleanFeatures=convertFeature(cleanVideoPath)
trainNet(netParams,maxIter,maxError,moment,cleanLabels,cleanFeatures)
