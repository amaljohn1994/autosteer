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
        correct=correctLabels[i].argmax(-1)+1
        if prediction[0]==correct:
            count=count+1
        i=i+1
    print "Correct Predictions: %d" %count
    a= float((float(count)/float(i))*100)
    print "Accuracy: %f" %a


def loadLabels():
    print "Select path for labels"
    root=tk.Tk()
    root.withdraw()
    fileName=filedialog.askopenfilename()
    cleanLabels=np.loadtxt(fileName)
    print cleanLabels.shape
    return cleanLabels

def loadFeatures():
    print "Select path for features"
    root=tk.Tk()
    root.withdraw()
    fileName=filedialog.askopenfilename()
    cleanFeatures=np.loadtxt(fileName)
    print cleanFeatures.shape
    return cleanFeatures

def loadCorrectLabels():
    print "Select path for correct labels"
    root=tk.Tk()
    root.withdraw()
    fileName=filedialog.askopenfilename()
    cleanLabels=np.loadtxt(fileName)
    print cleanLabels.shape
    return cleanLabels

def loadTrainingFeatures():
    print "Select path for training features"
    root=tk.Tk()
    root.withdraw()
    fileName=filedialog.askopenfilename()
    cleanFeatures=np.loadtxt(fileName)
    print cleanFeatures.shape
    return cleanFeatures

netParams=setNetParams()
maxIter,maxError,scale=setTrainParams()
cleanLabels=loadLabels()
cleanFeatures=loadFeatures()
xml_name=trainNet(netParams,maxIter,maxError,scale,cleanLabels,cleanFeatures)
