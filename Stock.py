import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar
from datetime import datetime, timedelta
class Stock:
    def __init__(self,stockName="AAL",path=""):
        self.stockName=stockName
        self.stockdir=self.generate(path)
        self.df=pd.read_csv(self.stockdir[stockName])
        self.date=self.df.iloc[:,0].values.astype("datetime64")
        self.open_price=self.df.iloc[:,1].values
        self.high_price=self.df.iloc[:,2].values
        self.low_price=self.df.iloc[:,3].values
        self.close_price=self.df.iloc[:,4].values
        self.volume=self.df.iloc[:,5].values
    def generate(self,path):
        stockdir={}
        p=path
        for i in os.listdir(p):
            stockname=i.split("_")[0]
            stockdir[stockname]=p+"/"+i
        return stockdir
    def linePlot(self, openn=True, close=True, high=False, low=False, volume=False, start=0, end=100):
        fig,ax = plt.subplots(figsize=(5, 2))
        plots = []
        if openn:
            plots.append(ax.plot(self.date[start:end], self.open_price[start:end], label="Open", color="blue")[0])
        if close:
            plots.append(ax.plot(self.date[start:end], self.close_price[start:end], label="Close", color="orange")[0])
        if high:
            plots.append(ax.plot(self.date[start:end], self.high_price[start:end], label="High", color="green")[0])
        if low:
            plots.append(ax.plot(self.date[start:end], self.low_price[start:end], label="Low", color="yellow")[0])
        if volume:
            plots.append(ax.plot(self.date[start:end], self.volume[start:end], label="Volume", color="red")[0])
        ax.set_xlabel("Date")
        ax.set_ylabel("Values")
        ax.set_title("Line plot: "+self.stockName)
        ax.legend(handles=plots)
        fig.set_facecolor('lightgray')
        ax.set_facecolor('lightgray')
        plt.xticks(rotation=45)
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=8)
        plt.xticks(rotation=45)
        return fig
