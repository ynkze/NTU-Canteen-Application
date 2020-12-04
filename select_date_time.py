# Run MainPage instead, this file is for importing to MainPage

from tkinter import *
import datetime
from dictionary import miniwok, indianfood, malaybbq, banmian, westernfood, drink, mcdonald
from waiting_time import waiting_time
from operatingtime import operating_time_miniwok, operating_time_indianfood, operating_time_malaybbq, \
    operating_time_banmian, operating_time_westernfood, operating_time_drink, operating_time_mcdonald


# define a function which will give raise to a new window on click
def raise_frame(frame):
    frame.tkraise()


def input_date_window():
    # global variables to make these accessible inside other functions
    global date
    global entry1, entry2, entry3, entry4, entry5
    global mainmenu_image
    global menuimage

    # images
    mainmenu_image = PhotoImage(file="list_of_stores.gif")
    menuimage = PhotoImage(file="menuimage.gif")

    # date picker window settings
    date = Tk()
    date.title("Enter Date and Time")
    date.geometry("480x150+400+400")

    # create two frame inside a window to separate the button and entry widget
    topFrame = Frame(date)# we place the entry widget and also the label inside the topframe so that it will be neater
    topFrame.pack()
    bottomFrame = Frame(date)# the confirm and quit button is place at the bottom frame to make the window neat
    bottomFrame.pack(side=BOTTOM)

    #label function is to display a words inside the frame
    #entry function is use to create an entry box inside the frame
    #here we use grid function to arrange the entry box and the label to make it look neat
    label1 = Label(topFrame, text="Select a date")
    label1.grid(row=0, column=3, columnspan=2)
    entry1 = Entry(topFrame, width=10)
    entry1.grid(row=1, column=0)
    label2 = Label(topFrame, text="/")
    label2.grid(row=1, column=2)
    label6 = Label(topFrame, text="(dd)")
    label6.grid(row=1, column=1)
    entry2 = Entry(topFrame, width=10)
    entry2.grid(row=1, column=3)
    label3 = Label(topFrame, text="/")
    label3.grid(row=1, column=5)
    label7 = Label(topFrame,text="(mm)")
    label7.grid(row=1, column=4)
    entry3 = Entry(topFrame, width=10)
    entry3.grid(row=1, column=6)
    label8 = Label(topFrame,text="(yy)")
    label8.grid(row=1, column=7)

    label4 = Label(topFrame, text="Select a time")
    label4.grid(row=2, column=3, columnspan=2)

    entry4 = Entry(topFrame, width=10)
    entry4.grid(row=3, column=3)
    label9 = Label(topFrame, text="(hr)")
    label9.grid(row=3, column=4)
    label10 = Label(topFrame, text=":")
    label10.grid(row=3, column=5)
    entry5 = Entry(topFrame, width=10)
    entry5.grid(row=3,column=6)
    label9 = Label(topFrame, text="(min)")
    label9.grid(row=3, column=7)
    label12 = Label(topFrame, text="(Enter time in 24 hour Format)")
    label12.grid(row=4,column=2,columnspan=4)

    button_confirm = Button(bottomFrame, text="Confirm", command=open_menu)
    button_confirm.pack(side=LEFT)
    button_quit = Button(bottomFrame, text="Exit", command=date.destroy)
    button_quit.pack(side=LEFT)


def open_menu():
    #create a toplevel instead of another root window because we only need one main program
    top = Toplevel()
    top.title("Canteen Manager")
    top.geometry("420x720+450+0")

    try:
        # get data entry from the entry box and change it into integer format
        day = entry1.get()
        day = int(day)
        month = entry2.get()
        month = int(month)
        year = entry3.get()
        year = int(year)
        hour = entry4.get()
        hour = int(hour)
        minute = entry5.get()
        minute = int(minute)
        date_get = datetime.datetime(year, month, day)
        # it will return weekday in the form of integer 0,1,2,3,4,5
        the_day_date = date_get.weekday()
        # change the date input into week name format
        days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
        #returns the days in weekday format
        the_days = days[the_day_date]
        if minute<10:
            minute = "0" + str(minute)
        if 0<=hour<12:
            date_today = [the_days, ",", year, "/", month, "/", day, ",", hour, ":", minute,"AM"]
        elif 12<=hour<=23:
            date_today = [the_days, ",", year, "/", month, "/", day, ",", hour, ":", minute, "PM"]

        if hour >= 24:
            raise ValueError

        date.destroy()
        # mcdonald frame with pictures and geometry
        mcdonald_frame = Frame(top)
        mcdonald_frame.place(x=0, y=0, width=420, height=720)

        mcdonald_canvas = Canvas(mcdonald_frame, width=420, height=720)
        mcdonald_canvas.pack(fill=BOTH, expand=1)
        mcdonald_canvas.create_image(200, 360, image=menuimage)

        mcdonald_menu_frame = Frame(mcdonald_frame, bg="gray8")
        mcdonald_menu_frame.place(x=60, y=200, width=300, height=350)

        Button(mcdonald_frame, text="QUIT", command=lambda: raise_frame(menu_frame)).place(x=180, y=600)
        Button(mcdonald_frame, text="Operating Hours", command=operating_time_mcdonald).place(x=100, y=150)
        Button(mcdonald_frame, text="Waiting Time", command=waiting_time).place(x=210, y=150)

        # unavailable operating hours
        if 0 <= hour < 6:
            Label(mcdonald_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

        # breakfast menu
        elif (0 <= the_day_date <= 6) and (6 <= hour < 12):
            for i in range(5, 7):
                Label(mcdonald_menu_frame, text=mcdonald[i],bg="gray8",fg="white").pack()

        # regular menu
        elif (0 <= the_day_date <= 6) and (12 <= hour <= 23):
            for i in range(0, 5):
                Label(mcdonald_menu_frame, text=mcdonald[i],bg="gray8",fg="white").pack()

        # miniwok frame with pictures and geometry
        miniwok_frame = Frame(top)
        miniwok_frame.place(x=0, y=0, width=420, height=720)

        miniwok_canvas = Canvas(miniwok_frame, width=420, height=720)
        miniwok_canvas.pack(fill=BOTH, expand=1)
        miniwok_canvas.create_image(200, 360, image=menuimage)


        miniwok_menu_frame = Frame(miniwok_frame, bg="gray8")
        miniwok_menu_frame.place(x=60, y=200, width=300, height=350)


        Button(miniwok_frame, text="QUIT", command=lambda: raise_frame(menu_frame)).place(x=180, y=600)
        Button(miniwok_frame, text="Operating Hours", command=operating_time_miniwok).place(x=100, y=150)
        Button(miniwok_frame, text="Waiting Time", command=waiting_time).place(x=210, y=150)

        # unavailable operating hours
        if 0 <= the_day_date <= 4 and (0 <= hour < 10 or 18 <= hour <= 23):
            Label(miniwok_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

        elif the_day_date == 5 and (0 <= hour < 10 or 14 <= hour <= 23):
            Label(miniwok_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

        # special menu for wednesday
        elif the_day_date == 2 and 10 <= hour < 18:
            for i in range(len(miniwok)):
                Label(miniwok_menu_frame, text=miniwok[i],bg="gray8",fg="white").pack()

        # normal menu
        elif the_day_date != 2 and 10 <= hour < 18:
            for i in range(2, 7):
                Label(miniwok_menu_frame, text=miniwok[i],bg="gray8",fg="white").pack()

        # indianfood frame with pictures and geometry
        indianfood_frame = Frame(top)
        indianfood_frame.place(x=0, y=0, width=420, height=720)

        indianfood_canvas = Canvas(indianfood_frame, width=420, height=720)
        indianfood_canvas.pack(fill=BOTH, expand=1)
        indianfood_canvas.create_image(200, 360, image=menuimage)

        indianfood_menu_frame = Frame(indianfood_frame, bg="gray8")
        indianfood_menu_frame.place(x=60, y=200, width=300, height=350)

        Button(indianfood_frame, text="QUIT", command=lambda: raise_frame(menu_frame)).place(x=180, y=600)
        Button(indianfood_frame, text="Operating Hours", command=operating_time_indianfood).place(x=100, y=150)
        Button(indianfood_frame, text="Waiting Time", command=waiting_time).place(x=210, y=150)

        # unavailable operating hours
        if 0 <= the_day_date <= 4 and (0 <= hour < 8 or 17 <= hour <= 23):
            Label(indianfood_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

        elif the_day_date == 5 and (0 <= hour < 8 or 13 <= hour <= 23):
            Label(indianfood_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

        # special menu for wednesday
        elif the_day_date == 2 and 8 <= hour < 17:
            for i in range(len(indianfood)):
                Label(indianfood_menu_frame, text=indianfood[i],bg="gray8",fg="white").pack()
        # normal menu
        elif the_day_date != 2 and 8 <= hour < 17:
            for i in range(0, 4):
                Label(indianfood_menu_frame, text=indianfood[i],bg="gray8",fg="white").pack()

        # malaybbq frame with geometry and pictures
        malaybbq_frame = Frame(top)
        malaybbq_frame.place(x=0, y=0, width=420, height=720)

        malaybbq_canvas = Canvas(malaybbq_frame, width=420, height=720)
        malaybbq_canvas.pack(fill=BOTH, expand=1)
        malaybbq_canvas.create_image(200, 360, image=menuimage)

        malaybbq_menu_frame = Frame(malaybbq_frame, bg="gray8")
        malaybbq_menu_frame.place(x=60, y=200, width=300, height=350)

        Button(malaybbq_frame, text="QUIT", command=lambda: raise_frame(menu_frame)).place(x=180, y=600)
        Button(malaybbq_frame, text="Operating Hours", command=operating_time_malaybbq).place(x=100, y=150)
        Button(malaybbq_frame, text="Waiting Time", command=waiting_time).place(x=210, y=150)

        # unavailable operating hours
        if 0 <= the_day_date <= 4 and (0 <= hour < 10 or 18 <= hour <= 23):
            Label(malaybbq_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

        elif the_day_date == 5 and (0 <= hour < 10 or 14 <= hour <= 23):
            Label(malaybbq_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

        # breakfast menu
        elif 0 <= the_day_date <= 5 and 10 <= hour < 12:
            for i in range(4, 5):
                Label(malaybbq_menu_frame, text=malaybbq[i],bg="gray8",fg="white").pack()

        # normal menu
        elif 0 <= the_day_date <= 4 and 12 <= hour < 18:
            for i in range(0, 4):
                Label(malaybbq_menu_frame, text=malaybbq[i],bg="gray8",fg="white").pack()

        elif the_day_date == 5 and 12 <= hour < 14:
            for i in range(0, 4):
                Label(malaybbq_menu_frame, text=malaybbq[i],bg="gray8",fg="white").pack()


        # banmian frame with geometry and pictures
        banmian_frame = Frame(top)
        banmian_frame.place(x=0, y=0, width=420, height=720)

        banmian_canvas = Canvas(banmian_frame, width=420, height=720)
        banmian_canvas.pack(fill=BOTH, expand=1)
        banmian_canvas.create_image(200, 360, image=menuimage)

        banmian_menu_frame = Frame(banmian_frame, bg="gray8")
        banmian_menu_frame.place(x=60, y=200, width=300, height=350)

        Button(banmian_frame, text="QUIT", command=lambda: raise_frame(menu_frame)).place(x=180, y=600)
        Button(banmian_frame, text="Operating Hours", command=operating_time_banmian).place(x=100, y=150)
        Button(banmian_frame, text="Waiting Time", command=waiting_time).place(x=210, y=150)

        # unavailable operating hours
        if 0 <= the_day_date <= 4 and (0 <= hour < 10 or 18 <= hour <= 23):
            Label(banmian_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

        elif the_day_date == 5 and (0 <= hour < 10 or 14 <= hour <= 23):
            Label(banmian_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

        # menu
        elif 0 <= the_day_date <= 4 and 10 <= hour < 18:
            for i in range(len(banmian)):
                Label(banmian_menu_frame, text=banmian[i],bg="gray8",fg="white").pack()

        elif the_day_date == 5 and 10 <= hour < 14:
            for i in range(len(banmian)):
                Label(banmian_menu_frame, text=banmian[i],bg="gray8",fg="white").pack()

        # westernfood frame with geometry and pictures
        westernfood_frame = Frame(top)
        westernfood_frame.place(x=0, y=0, width=420, height=720)

        westernfood_canvas = Canvas(westernfood_frame, width=420, height=720)
        westernfood_canvas.pack(fill=BOTH, expand=1)
        westernfood_canvas.create_image(200, 360, image=menuimage)

        westernfood_menu_frame = Frame(westernfood_frame, bg="gray8")
        westernfood_menu_frame.place(x=60, y=200, width=300, height=350)

        Button(westernfood_frame, text="QUIT", command=lambda: raise_frame(menu_frame)).place(x=180, y=600)
        Button(westernfood_frame, text="Operating Hours", command=operating_time_westernfood).place(x=100, y=150)
        Button(westernfood_frame, text="Waiting Time", command=waiting_time).place(x=210, y=150)

        # unavailable operating hours
        if 0 <= the_day_date <= 4 and (0 <= hour < 10 or 18 <= hour <= 23):
            Label(westernfood_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

        elif the_day_date == 5 and (0 <= hour < 10 or 14 <= hour <= 23):
            Label(westernfood_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

        # breakfast menu
        elif 0 <= the_day_date <= 5 and 10 <= hour < 12:
            for i in range(2, 4):
                Label(westernfood_menu_frame, text=westernfood[i],bg="gray8",fg="white").pack()

        # normal menu
        elif the_day_date == 5 and 12 <= hour < 14:
            for i in range(2):
                Label(westernfood_frame, text=westernfood[i],bg="gray8",fg="white").pack()

        elif 0 <= the_day_date <= 4 and 12 <= hour < 18:
            for i in range(2):
                Label(westernfood_menu_frame, text=westernfood[i],bg="gray8",fg="white").pack()

        # drink frame with geometry and pictures
        drink_frame = Frame(top)
        drink_frame.place(x=0, y=0, width=420, height=720)

        drink_canvas = Canvas(drink_frame, width=420, height=720)
        drink_canvas.pack(fill=BOTH, expand=1)
        drink_canvas.create_image(200, 360, image=menuimage)

        drink_menu_frame = Frame(drink_frame, bg="gray8")
        drink_menu_frame.place(x=10, y=200, width=400, height=350)

        Button(drink_frame, text="QUIT", command=lambda: raise_frame(menu_frame)).place(x=180, y=600)
        Button(drink_frame, text="Operating Hours", command=operating_time_drink).place(x=100, y=150)
        Button(drink_frame, text="Waiting Time", command=waiting_time).place(x=210, y=150)

        # unavailable operating hours
        if 0 <= the_day_date <= 4 and (0 <= hour < 7 or 20 <= hour <= 23):
            Label(drink_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

        elif the_day_date == 5 and (0 <= hour < 7 or 12 <= hour <= 23):
            Label(drink_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

        # breakfast menu
        elif 0 <= the_day_date <= 5 and 7 <= hour < 12:
            for i in range(3, 5):
                Label(drink_menu_frame, text=drink[i],bg="gray8",fg="white").pack()

        # normal menu
        elif 0 <= the_day_date <= 4 and 13 <= hour < 20:
            for i in range(0, 3):
                Label(drink_menu_frame, text=drink[i],bg="gray8",fg="white").pack()


        menu_frame = Frame(top)
        menu_frame.place(x=0, y=0, width=420, height=720)

        mainframe_canvas = Canvas(menu_frame, width=420, height=720, bg="white")
        mainframe_canvas.pack(fill=BOTH, expand=1)
        mainframe_canvas.create_image(200, 360, image=mainmenu_image)

        mainframe_canvas.create_text(200, 600, text=date_today, font="Arial 12 bold", fill="white")

        if 0 <= the_day_date <= 5:

            Button(mainframe_canvas, text="MCDONALD", width=12, command=lambda: raise_frame(mcdonald_frame), bg="black",
                   fg="white").place(x=150, y=200)
            Button(mainframe_canvas, text="DRINKS STALL", width=12, command=lambda: raise_frame(drink_frame),
                   bg="black", fg="white").place(x=150, y=250)
            Button(mainframe_canvas, text="INDIAN FOOD", width=12, command=lambda: raise_frame(indianfood_frame),
                   bg="black", fg="white").place(x=150, y=300)
            Button(mainframe_canvas, text="MALAYBBQ", width=12, command=lambda: raise_frame(malaybbq_frame), bg="black",
                   fg="white").place(x=150, y=350)
            Button(mainframe_canvas, text="BAN MIAN", width=12, command=lambda: raise_frame(banmian_frame), bg="black",
                   fg="white").place(x=150, y=400)
            Button(mainframe_canvas, text="WESTERN", width=12, command=lambda: raise_frame(westernfood_frame),
                   bg="black", fg="white").place(x=150, y=450)
            Button(mainframe_canvas, text="MINIWOK", width=12, command=lambda: raise_frame(miniwok_frame), bg="black",
                   fg="white").place(x=150, y=500)

        elif the_day_date == 6:
            Button(mainframe_canvas, text="MC DONALD", width=12, command=lambda: raise_frame(mcdonald_frame), bg="black", fg="white").place(x=150, y=200)

    except ValueError:
        top.destroy()
        exception = Toplevel()
        exception.title("Error")
        exception.geometry("200x50+500+450")
        error_message = Label(exception, text="Please enter a valid date and time!")
        error_message.pack()
        quitframe = Frame(exception)
        quitframe.pack(side=BOTTOM)
        quitbutton = Button(quitframe, text="Quit", command=exception.destroy)
        quitbutton.pack(side=LEFT)
