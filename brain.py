import Tkinter as tk
import tkFileDialog as filedialog
import numpy as np
import cv2
import cv2.cv as cv
import time

labelpath=""
featurepath=""

def chooseLabelPath():
    print "Select path for labels"
    root=tk.Tk()
    root.withdraw()
    labelpath=filedialog.askopenfilename()

def chooseFeaturePath():
    print "Select path for features"
    root=tk.Tk()
    root.withdraw()
    featurepath=filedialog.askopenfilename()

def
