# Autoclicker built with tkinter and pyautogui.

# Solution for keeping screen on top was googled. ): (Line 38)

import tkinter
from tkinter import *
import pydirectinput
import time
import threading


version = "Autoclicker 1.0.0 | Maintained by coolpancakes"
status = None


def auto_clicker():
    while True:
        if status == "disabled":
            exit()
        else:
            pydirectinput.click(interval=-0, clicks=100)


def threads(key_log):
    global status
    activation_key = str(key_log).split()[3]
    activation_key = activation_key.strip("keysym=")
    if activation_key == "F4":
        status = "enabled"
        auto = threading.Thread(target=auto_clicker)
        auto.start()
    elif activation_key == "F3":
        status = "disabled"


def main():
    root = Tk()
    root.wm_attributes("-topmost", True)
    root.geometry("350x170")
    root.title("Autoclicker")
    root.iconbitmap("mouse.ico")
    root.config(bg="black")
    version_info = Label(text=version, padx=10, pady=10, fg="grey", bg="black")
    clicker_status = Label(text="", fg="grey", bg="black")

    # Start button
    start = Button(text="F4 | Start/Stop", bg="black", fg="grey", pady=10, padx=10)

    # Bindings
    root.bind("<Key>", threads)

    # Packed widgets
    version_info.pack(side=TOP, fill=X)
    clicker_status.pack(fill=X)
    start.pack(side=TOP)
    root.mainloop()


if __name__ == "__main__":
    main()

# Add a status label that tells the user if the autoclicker is enabled or not.
# Fix the autoclicker, add functionality.
# Clean the code up make it more readable (rewrite variable names)
