import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar
from datetime import datetime, timedelta
from Stock import Stock
from DateSelector import DateSelectorApp
class PlotPage:
    def __init__(self, root,path):
        #main window definition
        self.root = root
        self.root.title("Plot Page")
        self.root.configure(background="light gray")
        window_width = root.winfo_screenwidth()
        window_height = root.winfo_screenheight()
        self.root.geometry(f"{window_width}x{window_height}")

        #Checkboxes
        self.checkLabel=tk.Label(root,text="Choose:",font = ("Helvetica", 10),background="light gray" )
        self.openvar=tk.IntVar(root)
        self.closevar=tk.IntVar(root)
        self.highvar=tk.IntVar(root)
        self.lowvar=tk.IntVar(root)
        self.volumevar=tk.IntVar(root)
        self.openCheck=tk.Checkbutton(root, text="Open",variable=self.openvar,background="light gray")
        self.closeCheck=tk.Checkbutton(root, text="Close",variable=self.closevar,background="light gray")
        self.highCheck=tk.Checkbutton(root, text="High",variable=self.highvar,background="light gray")
        self.lowCheck=tk.Checkbutton(root, text="Low",variable=self.lowvar,background="light gray")
        self.volumeCheck=tk.Checkbutton(root, text="Volume",variable=self.volumevar,background="light gray")


        
        #important variables
        self.plot="Line Plot"
        self.path=path
        self.stockName=""
        
        #selecting stock's name - Load
        self.stockLabel=tk.Label(root,text="Stock name",font = ("Helvetica", 10),background="light gray")
        self.stocks=Stock(path=self.path)
        options=list(self.stocks.stockdir)
        self.selected_stock=tk.StringVar()
        self.dropdown=ttk.Combobox(root,textvariable=self.selected_stock,values=options,background="light gray")
        self.select_button = tk.Button(root, text="Load", command=self.selectStock)
 
        
        #Plot
        self.select_button_plot = tk.Button(root,height=window_height//300,width=window_width//100,text="Plot", command=self.showPlot)
        self.canvas=None
        
        #Date
        self.from_date = None
        self.to_date = None
        self.from_date_label = tk.Label(root, text=" ",background="light gray")
        self.from_date_button = tk.Button(root, text="Select From Date", command=self.selectFrom)
        self.to_date_label = tk.Label(root, text=" ",background="light gray")
        self.to_date_button = tk.Button(root, text="Select To Date", command=self.selectTo)
        self.calendarFrom,self.calendarTo= None,None
        
        #Positioning
        center_x =  window_width // 2
        center_y = window_height // 2
        self.checkLabel.place(x=center_x+150,y=center_y-355)
        self.stockLabel.place(x=center_x-35,y=center_y-355)
        self.dropdown.place(x=center_x-70, y=center_y - 330)
        self.select_button.place(x=center_x-20, y=center_y - 300)
        self.from_date_button.place(x=center_x - 110, y=center_y - 260)
        self.from_date_label.place(x=center_x - 110, y=center_y - 230)
        self.to_date_button.place(x=center_x + 10, y=center_y - 260)
        self.to_date_label.place(x=center_x + 10, y=center_y - 230)
        self.openCheck.place(x=center_x + 150, y=center_y - 320, anchor=tk.W)
        self.closeCheck.place(x=center_x + 150, y=center_y - 290, anchor=tk.W)
        self.highCheck.place(x=center_x + 150, y=center_y - 260, anchor=tk.W)
        self.lowCheck.place(x=center_x + 150, y=center_y - 230, anchor=tk.W)
        self.volumeCheck.place(x=center_x + 150, y=center_y - 200, anchor=tk.W)
        self.select_button_plot.place(x=center_x-20, y=center_y + 270)

        
    def selectFrom(self):
        root=tk.Tk()
        l=[]
        self.calendarFrom =DateSelectorApp(root,self.stocks.date)
        root.mainloop()
    def selectTo(self):
        root=tk.Tk()
        self.calendarTo =DateSelectorApp(root,self.stocks.date)
        root.mainloop()
    
    def selectStock(self):
        self.stockName = self.dropdown.get()
        self.stocks=Stock(self.stockName,self.path)
    def createPlot(self):

        self.from_date=self.calendarFrom.selected
        self.to_date=self.calendarTo.selected
        start=np.where(self.stocks.date == self.from_date)[0][0]
        end=np.where(self.stocks.date== self.to_date)[0][0]
        fig=self.stocks.linePlot(self.openvar.get(),self.closevar.get(),self.highvar.get(),self.lowvar.get(),self.volumevar.get(),start,end)
        return fig
    def showPlot(self):
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()
        center_x =  window_width // 2
        center_y = window_height // 2
        if self.canvas:
            self.canvas.get_tk_widget().destroy()        
        fig = self.createPlot()
        self.from_date_label["text"]="From: "+str(self.from_date)
        self.to_date_label["text"]="To: "+str(self.to_date)
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.get_tk_widget().configure(width=600, height=450)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=center_x-280,y=center_y-190)

