import Tkinter as tk
import tkFileDialog as filedialog

def file():
    root=tk.Tk()
    root.withdraw()
    file_path=filedialog.askopenfilename()
    return file_path
