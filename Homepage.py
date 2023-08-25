import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar
from datetime import datetime, timedelta
from PlotPage import PlotPage
class HomePage:
    def __init__(self, root):
        root.title("Homepage")

        window_width = root.winfo_screenwidth()
        window_height = root.winfo_screenheight()
        root.geometry(f"{window_width}x{window_height}")

        self.plot = tk.Button(height=window_height//100,width=window_width//50, text="Plot", command=self.plotPage)
        self.predict = tk.Button(height=window_height//100,width=window_width//50, text="Predict", command=self.predictPage)
        self.plotpredict = tk.Button(height=window_height//100,width=window_width//50, text="Plot Predicted", command=self.predictPlotPage)

        pad=window_width//10
        self.plot.pack(side=tk.LEFT,padx=pad)
        self.predict.pack(side=tk.LEFT,padx=pad)
        self.plotpredict.pack(side=tk.LEFT,padx=pad)
    def plotPage(self):
        root = tk.Tk()
        app = PlotPage(root,os.getcwd().replace("\\","/")+"/"+"individual_stocks_5yr/individual_stocks_5yr")
        root.mainloop()
    def predictPage(self):
        print("Page2")
    def predictPlotPage(self):
        print("Page3")
root = tk.Tk()
app = HomePage(root)
root.mainloop()
    