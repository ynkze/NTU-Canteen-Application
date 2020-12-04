# Run this, other files are for importing into here

from tkinter import *
import datetime
from select_date_time import input_date_window
from waiting_time import waiting_time
from dictionary import miniwok, indianfood, malaybbq, banmian, westernfood, drink, mcdonald
from operatingtime import operating_time_miniwok, operating_time_indianfood, operating_time_malaybbq, \
    operating_time_banmian, operating_time_westernfood, operating_time_drink, operating_time_mcdonald

# main window settings and defining pictures
root = Tk()
root.geometry("800x600+250+50")#geometry of the window, widthxheight and the plus is the starting position of the window
root.title("Canteen Manager")#the title of the window
#assign the images file to a variable
background_image = PhotoImage(file="background.gif")
mainpageimage = PhotoImage(file="list_of_stores.gif")
menuimage = PhotoImage(file="menuimage.gif")

HEIGHT = 800
WIDTH = 600


# define a function which will give raise to a new window on click
def raise_frame(frame):
    frame.tkraise()


# create a new window on click of todaydatetime
def today_menu():
    # get the weekday today in the form of integer of 0 to 6
    today_day = datetime.datetime.today().weekday()
    # get the time now(build in function datetime)
    date_get = datetime.datetime.now()
    # convert the hour now into string format and then integer using strftime built in function
    current_hour = date_get.strftime('%H')
    current_hour = int(current_hour)

    # main window
    show_today_menu_window = Toplevel(root)
    show_today_menu_window.geometry("420x720+450+0")

    # mcdonald frame with pictures and geometry
    mcdonald_frame = Frame(show_today_menu_window)
    mcdonald_frame.place(x=0, y=0, width=420, height=720)

    #create a canvas inside the frame of the main window to add background image
    mcdonald_canvas = Canvas(mcdonald_frame, width=WIDTH, height=HEIGHT, bg="white")
    mcdonald_canvas.pack(fill=BOTH, expand=1)#using the geometry manager "pack"
    mcdonald_canvas.create_image(200, 360, image=menuimage)#using the function create image to create an image inside a canvas
    #create another frame inside the canvas to put in label
    mcdonald_menu_frame = Frame(mcdonald_frame, bg="gray8")
    mcdonald_menu_frame.place(x=60, y=200, width=300, height=350)

    # buttons
    Button(mcdonald_frame, text="BACK", command=lambda: raise_frame(main_frame)).place(x=180, y=600)
    Button(mcdonald_frame, text="Operating Hours", command=operating_time_mcdonald).place(x=100, y=150)
    Button(mcdonald_frame, text="Waiting Time", command=waiting_time).place(x=210, y=150)

    # unavailable operating hours
    if 0 <= current_hour < 6:
        Label(mcdonald_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

    # breakfast menu
    elif 0 <= today_day <= 6 and 6 <= current_hour < 12:
        for i in range(5, 7):
            Label(mcdonald_menu_frame, text=mcdonald[i],bg="gray8",fg="white").pack()

    # regular menu
    elif 0 <= today_day <= 6 and 12 <= current_hour <= 23:
        for i in range(0, 5):
            Label(mcdonald_menu_frame, text=mcdonald[i],bg="gray8",fg="white").pack()

    # miniwok frame with pictures and geometry
    miniwok_frame = Frame(show_today_menu_window)
    miniwok_frame.place(x=0, y=0, width=420, height=720)
    miniwok_canvas = Canvas(miniwok_frame, width=WIDTH, height=HEIGHT, bg="white")

    miniwok_canvas.pack(fill=BOTH, expand=1)
    miniwok_canvas.create_image(200, 360, image=menuimage)

    miniwok_menu_frame = Frame(miniwok_frame, bg="gray8")
    miniwok_menu_frame.place(x=60, y=200, width=300, height=350)

    # buttons
    Button(miniwok_frame, text="BACK", command=lambda: raise_frame(main_frame)).place(x=180, y=600)
    Button(miniwok_frame, text="Operating Hours", command=operating_time_miniwok).place(x=100, y=150)
    Button(miniwok_frame, text="Waiting Time", command=waiting_time).place(x=210, y=150)

    # unavailable operating hours
    if 0 <= today_day <= 4 and (0 <= current_hour < 10 or 18 <= current_hour <= 23):
        Label(miniwok_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

    elif today_day == 5 and (0 <= current_hour < 10 or 14 <= current_hour <= 23):
        Label(miniwok_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

    # special menu for wednesday
    elif today_day == 2 and 10 <= current_hour < 18:
        for i in range(len(miniwok)):
            Label(miniwok_menu_frame, text=miniwok[i],bg="gray8",fg="white").pack()

    # normal menu
    elif today_day != 2 and 10 <= current_hour < 18:
        for i in range(2, 7):
            Label(miniwok_menu_frame, text=miniwok[i],bg="gray8",fg="white").pack()

    # indianfood frame with pictures and geometry
    indianfood_frame = Frame(show_today_menu_window)
    indianfood_frame.place(x=0, y=0, width=420, height=720)

    indianfood_canvas = Canvas(indianfood_frame, width=WIDTH, height=HEIGHT, bg="white")
    indianfood_canvas.pack(fill=BOTH, expand=1)
    indianfood_canvas.create_image(200, 360, image=menuimage)

    indianfood_menu_frame = Frame(indianfood_frame, bg="gray8")
    indianfood_menu_frame.place(x=60, y=200, width=300, height=350)

    #buttons
    Button(indianfood_frame, text="BACK", command=lambda: raise_frame(main_frame)).place(x=180, y=600)
    Button(indianfood_frame, text="Operating Hours", command=operating_time_indianfood).place(x=100, y=150)
    Button(indianfood_frame, text="Waiting Time", command=waiting_time).place(x=210, y=150)

    # unavailable operating hours
    if 0 <= today_day <= 4 and (0 <= current_hour < 8 or 17 <= current_hour <= 23):
        Label(indianfood_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

    elif today_day == 5 and (0 <= current_hour < 8 or 13 <= current_hour <= 23):
        Label(indianfood_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

    # special menu for wednesday
    elif today_day == 2 and 8 <= current_hour < 17:
        for i in range(len(indianfood)):
            Label(indianfood_menu_frame, text=indianfood[i],bg="gray8",fg="white").pack()

    # normal menu
    elif today_day != 2 and 8 <= current_hour < 17:
        for i in range(0, 4):
            Label(indianfood_menu_frame, text=indianfood[i],bg="gray8",fg="white").pack()

    # malaybbq frame with geometry and pictures
    malaybbq_frame = Frame(show_today_menu_window)
    malaybbq_frame.place(x=0, y=0, width=420, height=720)

    malaybbq_canvas = Canvas(malaybbq_frame, width=WIDTH, height=HEIGHT, bg="white")
    malaybbq_canvas.pack(fill=BOTH, expand=1)
    malaybbq_canvas.create_image(200, 360, image=menuimage)

    malaybbq_menu_frame = Frame(malaybbq_frame, bg="gray8")
    malaybbq_menu_frame.place(x=60, y=200, width=300, height=350)

    # buttons
    Button(malaybbq_frame, text="BACK", command=lambda: raise_frame(main_frame)).place(x=180, y=600)
    Button(malaybbq_frame, text="Operating Hours", command=operating_time_malaybbq).place(x=100, y=150)
    Button(malaybbq_frame, text="Waiting Time", command=waiting_time).place(x=210, y=150)

    # unavailable operating hours
    if 0 <= today_day <= 4 and (0 <= current_hour < 10 or 18 <= current_hour <= 23):
        Label(malaybbq_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

    elif today_day == 5 and (0 <= current_hour < 10 or 14 <= current_hour <= 23):
        Label(malaybbq_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

    # breakfast menu
    elif 0 <= today_day <= 5 and 10 <= current_hour < 12:
        for i in range(4, 5):
            Label(malaybbq_menu_frame, text=malaybbq[i],bg="gray8",fg="white").pack()

    # normal menu
    elif 0 <= today_day <= 4 and 12 <= current_hour < 18:
        for i in range(0, 4):
            Label(malaybbq_menu_frame, text=malaybbq[i],bg="gray8",fg="white").pack()

    elif today_day == 5 and 12 <= current_hour < 14:
        for i in range(0, 4):
            Label(malaybbq_menu_frame, text=malaybbq[i],bg="gray8",fg="white").pack()

    # banmian frame with geometry and pictures
    banmian_frame = Frame(show_today_menu_window)
    banmian_frame.place(x=0, y=0, width=420, height=720)

    banmian_canvas = Canvas(banmian_frame, width=WIDTH, height=HEIGHT, bg="white")
    banmian_canvas.pack(fill=BOTH, expand=1)
    banmian_canvas.create_image(200, 360, image=menuimage)

    banmian_menu_frame = Frame(banmian_frame, bg="gray8")
    banmian_menu_frame.place(x=60, y=200, width=300, height=350)

    # buttons
    Button(banmian_frame, text="BACK", command=lambda: raise_frame(main_frame)).place(x=180, y=600)
    Button(banmian_frame, text="Operating Hours", command=operating_time_banmian).place(x=100, y=150)
    Button(banmian_frame, text="Waiting Time", command=waiting_time).place(x=210, y=150)

    # unavailable operating hours
    if 0 <= today_day <= 4 and (0 <= current_hour < 10 or 18 <= current_hour <= 23):
        Label(banmian_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

    elif today_day == 5 and (0 <= current_hour < 10 or 14 <= current_hour <= 23):
        Label(banmian_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

    # menu
    elif 0 <= today_day <= 4 and 10 <= current_hour < 18:
        for i in range(len(banmian)):
            Label(banmian_menu_frame, text=banmian[i],bg="gray8",fg="white").pack()

    elif today_day == 5 and 10 <= current_hour < 14:
        for i in range(len(banmian)):
            Label(banmian_menu_frame, text=banmian[i],bg="gray8",fg="white").pack()

    # westernfood frame with geometry and pictures
    westernfood_frame = Frame(show_today_menu_window)
    westernfood_frame.place(x=0, y=0, width=420, height=720)

    westernfood_canvas = Canvas(westernfood_frame, width=WIDTH, height=HEIGHT, bg="white")
    westernfood_canvas.pack(fill=BOTH, expand=1)
    westernfood_canvas.create_image(200, 360, image=menuimage)

    westernfood_menu_frame = Frame(westernfood_frame, bg="gray8")
    westernfood_menu_frame.place(x=60, y=200, width=300, height=350)

    # buttons
    Button(westernfood_frame, text="BACK", command=lambda: raise_frame(main_frame)).place(x=180, y=600)
    Button(westernfood_frame, text="Operating Hours", command=operating_time_westernfood).place(x=100, y=150)
    Button(westernfood_frame, text="Waiting Time", command=waiting_time).place(x=210, y=150)

    # unavailable operating hours
    if 0 <= today_day <= 4 and (0 <= current_hour < 10 or 18 <= current_hour <= 23):
        Label(westernfood_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

    elif today_day == 5 and (0 <= current_hour < 10 or 14 <= current_hour <= 23):
        Label(westernfood_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

    # breakfast menu
    elif 0 <= today_day <= 5 and 10 <= current_hour < 12:
        for i in range(2, 4):
            Label(westernfood_menu_frame, text=westernfood[i],bg="gray8",fg="white").pack()

    # normal menu
    elif today_day == 5 and 12 <= current_hour < 14:
        for i in range(2):
            Label(westernfood_frame, text=westernfood[i],bg="gray8",fg="white").pack()

    elif 0 <= today_day <= 4 and 12 <= current_hour < 18:
        for i in range(2):
            Label(westernfood_menu_frame, text=westernfood[i],bg="gray8",fg="white").pack()

    # drink frame with geometry and pictures
    drink_frame = Frame(show_today_menu_window)
    drink_frame.place(x=0, y=0, width=420, height=720)

    drink_canvas = Canvas(drink_frame, width=WIDTH, height=HEIGHT, bg="white")
    drink_canvas.pack(fill=BOTH, expand=1)
    drink_canvas.create_image(200, 360, image=menuimage)

    drink_menu_frame = Frame(drink_frame, bg="gray8")
    drink_menu_frame.place(x=60, y=200, width=300, height=350)

    # buttons
    Button(drink_frame, text="BACK", command=lambda: raise_frame(main_frame)).place(x=180, y=600)
    Button(drink_frame, text="Operating Hours", command=operating_time_drink).place(x=100, y=150)
    Button(drink_frame, text="Waiting Time", command=waiting_time).place(x=210, y=150)

    # unavailable operating hours
    if 0 <= today_day <= 4 and (0 <= current_hour < 7 or 20 <= current_hour <= 23):
        Label(drink_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

    elif today_day == 5 and (0 <= current_hour < 7 or 12 <= current_hour <= 23):
        Label(drink_menu_frame, text="No menu available at this time!",bg="gray8",fg="white").pack()

    # breakfast menu
    elif 0 <= today_day <= 5 and 7 <= current_hour < 12:
        for i in range(3, 5):
            Label(drink_menu_frame, text=drink[i],bg="gray8",fg="white").pack()

    # normal menu
    elif 0 <= today_day <= 4 and 12 <= current_hour < 20:
        for i in range(0, 3):
            Label(drink_menu_frame, text=drink[i],bg="gray8",fg="white").pack()

    # frame and canvas to contain buttons and images
    main_frame = Frame(show_today_menu_window)
    main_frame.place(width=420, height=720)

    mainframe_canvas = Canvas(main_frame, width=WIDTH, height=HEIGHT, bg="white")
    mainframe_canvas.pack(fill=BOTH, expand=1)
    mainframe_canvas.create_image(200, 360, image=mainpageimage)

    # display current date and time on the menu
    print_date = date_get.strftime("%a, %d %B %Y %I:%M%p")
    mainframe_canvas.create_text(200, 600, text=print_date, font="Arial 12 bold", fill="white")

    # display stores from Mon-Sat
    if 0 <= today_day <= 5:

        Button(mainframe_canvas, text="MCDONALD", width=12, command=lambda: raise_frame(mcdonald_frame), bg="black",
               fg="white").place(x=150, y=200)
        Button(mainframe_canvas, text="DRINKS STALL", width=12, command=lambda: raise_frame(drink_frame), bg="black",
               fg="white").place(x=150, y=250)
        Button(mainframe_canvas, text="INDIAN FOOD", width=12, command=lambda: raise_frame(indianfood_frame),
               bg="black", fg="white").place(x=150, y=300)
        Button(mainframe_canvas, text="MALAYBBQ", width=12, command=lambda: raise_frame(malaybbq_frame), bg="black",
               fg="white").place(x=150, y=350)
        Button(mainframe_canvas, text="BAN MIAN", width=12, command=lambda: raise_frame(banmian_frame), bg="black",
               fg="white").place(x=150, y=400)
        Button(mainframe_canvas, text="WESTERN", width=12, command=lambda: raise_frame(westernfood_frame), bg="black",
               fg="white").place(x=150, y=450)
        Button(mainframe_canvas, text="MINIWOK", width=12, command=lambda: raise_frame(miniwok_frame), bg="black",
               fg="white").place(x=150, y=500)

    # display only McDonald on Sunday
    elif today_day == 6:
        Button(mainframe_canvas, text="MCDONALD", width=12, command=lambda: raise_frame(mcdonald_frame), bg="black",
               fg="white").place(x=150, y=200)


# create a frame
BgFrame = Frame(bg="white")
BgFrame.pack(fill=BOTH, expand=1)

# create a canvas inside a frame
bgcanvas = Canvas(BgFrame, width=WIDTH, height=HEIGHT, bg="white")
bgcanvas.pack(fill=BOTH, expand=1)
bgcanvas.create_image(400, 300, image=background_image)

# create main buttons inside the background canvas
selectbutton = Button(text="Select Date and Time", width=20, command=input_date_window, bg="black", fg="white",
                      font="arial 15 bold").place(x=275, y=300)
selectbutton2 = Button(text="Show current menu", width=20, command=today_menu, bg="black", fg="white",
                       font="arial 15 bold").place(x=275, y=400)

# creates function for the buttons
bgcanvas.create_window(400, 400, window=selectbutton)
bgcanvas.create_window(400, 425, window=selectbutton2)

# title
bgcanvas.create_text(400, 200, text="North Spine Canteen Manager", font="Impact 30 bold", fill="white")

root.mainloop()
