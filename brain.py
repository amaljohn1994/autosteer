import Tkinter as tk
import tkFileDialog as filedialog
import numpy as np
import cv2
import cv2.cv as cv
import time

def setNetParams():
    t=int(raw_input("Total number of layers for network:"))
    netParams=np.zeros((1,t),'int32')
    for i in range(0,t):
        c=i+1
        netParams[0,i]=int(raw_input("Enter no. of neurons in layer %d:"%c))
    return netParams[0]

def setTrainParams():
    scale=float(raw_input("Enter moment scale:"))
    maxIter=int(raw_input("Enter maximum iterations:"))
    maxError=float(raw_input("Enter eror change to stop:"))
    return maxIter,maxError,scale

def trainNet(netParams,maxIter,maxError,scale,cleanLabels,cleanFeatures):
    model=cv2.ANN_MLP()
    model.create(netParams)
    criteria = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, maxIter, maxError)
    params = dict(term_crit = criteria,
                   train_method = cv2.ANN_MLP_TRAIN_PARAMS_BACKPROP,
                   bp_dw_scale = scale,
                   bp_moment_scale = 0.0 )
    num_iter=model.train(cleanFeatures,cleanLabels,None,params=params)
    print num_iter
    m=raw_input("Enter name of xml to save model:")
    model.save(m)
    """ Should return time taken for training"""

"""Write function to predict
given path to xml of net,path to test data,
return performance parameters, retrun time taken"""



netParams=setNetParams()
maxIter,maxError,scale=setTrainParams()
trainNet(netParams,maxIter,maxError,scale,cleanLabels,cleanFeatures)
