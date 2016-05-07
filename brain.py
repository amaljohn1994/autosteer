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
    print "Parameters set successfully..."
    return netParams[0]

def setTrainParams():
    scale=float(raw_input("Enter scale(=0.001):"))
    maxIter=int(raw_input("Enter maximum iterations(300):"))
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
    print "Training started..."
    num_iter=model.train(cleanFeatures,cleanLabels,None,params=params)
    print "Training completed in %d iterations..." %num_iter
    m=raw_input("Enter name of xml to save model(no ext. reqd):")
    model.save(m+".xml")
    print "File saved successfully..."
    return m+".xml"

def predict(fileName,layers):
    nnet=cv2.ANN_MLP()
    nnet.create(layers)
    nnet.load(fileName)
    correctLabels=loadCorrectLabels()
    trainingFeatures=loadTrainingFeatures()
    i=0
    count=0
    for feature in trainingFeatures:
        prediction=np.zeros((1,4),'float')
        test=np.zeros((0,76800),'float')
        test=feature.reshape((1,76800))
        test=test+0.00
        nnet.predict(test,prediction)
        prediction=prediction.argmax(-1)+1
        if prediction==correctLabels[i]
            count=count+1
        print 'Prediction:',prediction
        i=i+1
    print (count/i)*100

def loadLabels():
    fileName=raw_input("Enter filename containing labels(.npz reqd)):")
    cleanLabels=np.load(fileName)
    return cleanLabels['arr_0']

def loadFeatures():
    fileName=raw_input("Enter filename containing features(.npz reqd):")
    cleanFeatures=np.load(fileName)
    return cleanFeatures['arr_0']

def loadCorrectLabels():
    fileName=raw_input("Enter filename containing correct labels(.npz reqd)):")
    cleanLabels=np.load(fileName)
    return cleanLabels['arr_0']

def loadTrainingFeatures():
    fileName=raw_input("Enter filename containing training features(.npz reqd):")
    cleanFeatures=np.load(fileName)
    return cleanFeatures['arr_0']

netParams=setNetParams()
maxIter,maxError,scale=setTrainParams()
cleanLabels=loadLabels()
cleanFeatures=loadFeatures()
xml_name=trainNet(netParams,maxIter,maxError,scale,cleanLabels,cleanFeatures)
number=raw_input("Enter no. of sets to predict:")
for i in range(0,int(number)):
    predict(xml_name,netParams)
