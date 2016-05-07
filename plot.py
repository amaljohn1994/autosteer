import matplotlib.pyplot as plt
import numpy as np

def plot(labels):
    l=len(labels)
    t=np.arange(0.0,l,1)
    plt.plot(t,labels)
    plt.show()
    name=raw_input("Enter name to store plot(with .png):")
    plt.savefig(name)
