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

def loadXml():
    print "Select path for XML File"
    root=tk.Tk()
    root.withdraw()
    fileName=filedialog.askopenfilename()
    return fileName

netParams=setNetParams()
number=raw_input("Enter no. of sets to predict:")
for i in range(0,int(number)):
    predict(xml_name,netParams)
