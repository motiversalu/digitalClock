#! python 3
from tkinter import *
import time

root = Tk()  #main canvas
root.title("Metro Digital Clock")
root.geometry("600x300+400+250")
root.iconbitmap(r"C:\Users\TAHIRUSALIFU\Desktop\MY PYTHON LEARNING\Digitalclock_icon-icons.com_51170.ico")
root.configure(bg="grey")
root.resizable(False, False)  #window should not be resizable


#function to produce and update time
def timer():
    currentTime = time.strftime("%H:%M:%S")
    clock.configure(text=currentTime)
    clock.after(200, timer)


#other GUI for the screen of the clock
header = Label(root, text="M E T R O  D I G I T A L  C L O C K", bg="#1a52ed", fg="white", font=("times", 24, "bold"))
header.pack(expand=NO, fill=X, anchor="center", side=TOP, ipady=10)

clock = Label(root, bg="white", fg="black", font=("times", 20, "bold"))
clock.pack(anchor="center", fill=NONE, expand=NO, padx=20, pady=(20, 5), ipadx=90, ipady=30)
clock_legend = Label(text="Hours   Minutes   Seconds", bg="grey", fg="yellow", font=("times", 12, "bold"))
clock_legend.pack(pady=(3, 0), padx=(10, 10), anchor="center")
timer()

exitButton = Button(text="Exit", bg="red", fg="white", command=root.destroy)
exitButton.pack(side=BOTTOM, expand=NO, ipadx=20, pady=25, padx=30)

root.mainloop()
