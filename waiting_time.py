# Run MainPage instead, this file is for importing to MainPage

from tkinter import *
from tkinter import Button


def waiting_time():
    def show_waiting_time():
        try:
            # waiting time display window setup
            time = Toplevel()
            time.title("Waiting Time")
            time.geometry("230x50+500+450")

            # obtain the user input and multiply by estimated waiting time of 2
            ans = int(e1.get()) * 2

            # exception handling when user tries to enter a negative number
            if ans < 0:
                raise ValueError

            # display of estimated waiting time
            new_window = Label(time, text="The estimated waiting time is " + str(ans) + " minutes.")
            new_window.pack()

            # quit button
            quitframe = Frame(time)
            quitframe.pack()
            quitbutton = Button(quitframe, text="Quit", command=time.destroy)
            quitbutton.pack(side=BOTTOM)

        # exception handling with a new window to display error message
        except ValueError:
            time.destroy()
            exception = Toplevel()
            exception.title("Error")
            exception.geometry("200x50+500+450")

            error_message = Label(exception, text="Please enter a valid number!")
            error_message.pack()

            quitframe = Frame(exception)
            quitframe.pack(side=BOTTOM)
            quitbutton = Button(quitframe, text="Quit", command=exception.destroy)
            quitbutton.pack(side=LEFT)

    # waiting time input window set up
    master = Tk()
    master.title("Input")
    master.geometry("200x100+500+400")

    # prompt user to input number of people in queue
    Label(master, text="Enter number of people in queue:").pack()
    e1 = Entry(master)
    e1.pack()

    # confirm button
    confirmframe = Frame(master)
    confirmframe.pack()
    Button(confirmframe, text="Confirm", command=show_waiting_time).pack()

    # quit button
    quitframe = Frame(master)
    quitframe.pack()
    Button(quitframe, text="Quit", command=master.destroy).pack()

    master.mainloop()

