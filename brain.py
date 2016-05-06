from brain import clean_samples
import Tkinter as tk
import tkFileDialog as filedialog

print "Select path for labels"
root=tk.Tk()
root.withdraw()
labelpath=filedialog.askopenfilename()

print "Select path for features"
root=tk.Tk()
root.withdraw()
featurepath=filedialog.askopenfilename()
c=clean_samples(featurepath,labelpath)
c.clean()
