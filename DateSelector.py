import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar
from datetime import datetime, timedelta
class DateSelectorApp:
    def __init__(self,root,dates):
        self.root = root
        self.root.title("Date Selector")

        # Available days
        dates=dates.tolist()
        from_date = dates[0]
        to_date = dates[-1]
        unavailable_dates=self.generateUnavailableDates(from_date,to_date,dates)

        #Calendar widget
        self.calendar = Calendar(root, selectmode='day', mindate=from_date, maxdate=to_date, disabledays=unavailable_dates)
        self.calendar.pack(padx=20, pady=20)
        self.selected=None
        #Choose date
        self.get_date_button = tk.Button(root, text="Get Selected Date", command=self.getDate)
        self.get_date_button.pack(pady=10)
    def generateUnavailableDates(self,start_date, end_date,dates):
        udates = []
        current_date = start_date
        i=0
        while current_date <= end_date:
            if(current_date==dates[i]):
                i+=1
                current_date+=timedelta(days=1)
            else:
                udates.append(current_date)
                current_date += timedelta(days=1)
        return udates
    
    def getDate(self):
        try:
            selected_date = self.calendar.get_date()
            month,day,year=selected_date.split("/")
            if(len(day)==1):
                day="0"+day
            if(len(month)==1):
                month="0"+month
            month+="-"
            year="20"+year+"-"
            self.selected=np.datetime64(year+month+day)
            self.root.destroy()
        except:
            print("Date Not selected!")