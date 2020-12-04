# Run MainPage instead, this file is for importing to MainPage

from tkinter import *


def operating_time_miniwok():
    # create a new pop up window to show the operating time on click of a button
    operate_time = Toplevel()
    operate_time.title("Operating Time")
    operate_time.geometry("300x150+460+400")

    # print the operating time of the stall on the window using the label function
    with open("operatingtime.txt","r") as f:
        for i in range(0,3):
            miniwok_line = f.readline()
            if 0<=i<=3:
                operatelabel = Label(operate_time, text=miniwok_line)
                operatelabel.pack()

    # create a button inside the new pop up window call back to destroy the window
    Button(operate_time,text="BACK",command=operate_time.destroy).place(x=130,y=120)

def operating_time_indianfood():
    # create a new pop up wimdow to show the operating time on click of a button
    operate_time = Toplevel()
    operate_time.title("Operating Time")
    operate_time.geometry("300x150+460+400")

    # print the operating time of the stall on the window using the label function
    with open("operatingtime.txt","r") as f:
        for i in range(0,11):
            indianfood_line = f.readline()
            if 8<=i<=11:
                operatelabel = Label(operate_time, text=indianfood_line)
                operatelabel.pack()

    # create a button inside the new pop up window call back to destroy the window
    Button(operate_time,text="BACK",command=operate_time.destroy).place(x=130,y=120)

def operating_time_malaybbq():
    # create a new pop up wimdow to show the operating time on click of a button
    operate_time = Toplevel()
    operate_time.title("Operating Time")
    operate_time.geometry("300x150+460+400")

    with open("operatingtime.txt","r") as f:
        for i in range(0,3):
            malaybbq_line = f.readline()
            if 0<=i<=3:
                operatelabel = Label(operate_time, text=malaybbq_line)
                operatelabel.pack()

    # create a button inside the new pop up window call Back to destroy the window
    Button(operate_time,text="BACK",command=operate_time.destroy).place(x=130,y=120)

def operating_time_banmian():
    # create a new pop up wimdow to show the operating time on click of a button
    operate_time = Toplevel()
    operate_time.title("Operating Time")
    operate_time.geometry("300x150+460+400")

    with open("operatingtime.txt","r") as f:
        for i in range(0,3):
            banmian_line = f.readline()
            if 0<=i<=3:
                operatelabel = Label(operate_time, text=banmian_line)
                operatelabel.pack()

    # create a button inside the new pop up window call Back to destroy the window
    Button(operate_time,text="BACK",command=operate_time.destroy).place(x=130,y=120)

def operating_time_westernfood():
    # create a new pop up window to show the operating time on click of a button
    operate_time = Toplevel()
    operate_time.title("Operating Time")
    operate_time.geometry("300x150+460+400")

    with open("operatingtime.txt","r") as f:
        for i in range(0,3):
            western_line = f.readline()
            if 0<=i<=3:
                operatelabel = Label(operate_time, text=western_line)
                operatelabel.pack()

    # create a button inside the new pop up window call Back to destroy the window
    Button(operate_time,text="BACK",command=operate_time.destroy).place(x=130,y=120)

def operating_time_drink():
    # create a new pop up window to show the operating time on click of a button
    operate_time = Toplevel()
    operate_time.title("Operating Time")
    operate_time.geometry("300x150+460+400")

    with open("operatingtime.txt", "r") as f:
        for i in range(0, 16):
            drink_line = f.readline()
            if 12 <= i <= 16:
                operatelabel = Label(operate_time, text=drink_line)
                operatelabel.pack()

    # create a button inside the new pop up window call Back to destroy the window
    Button(operate_time,text="BACK",command=operate_time.destroy).place(x=130,y=120)

def operating_time_mcdonald():
    #  a new pop up window to show the operating time on click of a button
    operate_time = Toplevel()
    operate_time.title("Operating Time")
    operate_time.geometry("300x150+460+400")

    with open("operatingtime.txt", "r") as f:
        for i in range(0, 21):
            mcdonald_line = f.readline()
            if 16 <= i <= 21:
                operatelabel = Label(operate_time, text=mcdonald_line)
                operatelabel.pack()

    # create a button inside the new pop up window call Back to destroy the window
    Button(operate_time,text="BACK",command=operate_time.destroy).place(x=130,y=120)



