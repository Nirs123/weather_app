import weather_prevision
import tkinter as tk
from tkinter import *
from tkinter import ttk

win = tk.Tk()
win.title("Weather Prevision")
win.geometry("900x650")
win.minsize(900,650)
win.maxsize(900,650)
win.config(bg="#357aab")

twenty_four_hours_prevision = False
seven_days_prevision = False
fourteen_days_prevision = False

def gui_main():
    city_entry_var = tk.StringVar()
    city_entry = tk.Entry(win, font=('Segoe UI Black',"25"), textvariable=city_entry_var)
    go_button = tk.Button(win, font=('Segoe UI Black',"17"), text="GO", command = gui_prevision_selection)

    city_entry.grid(row=0,column=0,padx=10,pady=10)
    go_button.grid(row=0,column=1,padx=0)

frame1 = tk.Frame(bg="#357aab")
frame2 = tk.Frame(bg="#357aab")
def gui_prevision_selection():
    tfh_button = tk.Button(frame1, font=('Segoe UI Black',"19"),text="24 Hours", command=tfh_prevision)
    sd_button = tk.Button(frame1, font=('Segoe UI Black',"19"),text="7 Days", command=sd_prevision)
    fd_button = tk.Button(frame1, font=('Segoe UI Black',"19"),text="14 Days", command=fd_prevision)

    tfh_button.grid(row=2,column=0,padx=10,pady=10)
    sd_button.grid(row=2,column=1,padx=10,pady=0)
    fd_button.grid(row=2,column=2,padx=10,pady=0)

    frame1.grid()

def tfh_prevision():
    pass

def sd_prevision():
    pass

def fd_prevision():
    pass

gui_main()
win.mainloop()