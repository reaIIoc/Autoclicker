# Autoclicker built with tkinter and pyautogui.

import tkinter
from tkinter import *
import pydirectinput
import time
import threading
import win32api


version = "Autoclicker 1.0.1 | Maintained by datarec"
status = False


def auto_clicker():
    global status
    while True:
        parent = threading.main_thread()
        parent_status = str(parent).split(",")[1]
        key_press = win32api.GetKeyState(0x73)
        status = key_press
        if status == 0:
            pass
        elif "stopped" in parent_status:
            quit()
        elif status == 1:
            pydirectinput.click(interval=-0, clicks=1)


def main():
    root = Tk()
    root.geometry("350x170")
    root.title("Autoclicker")
    root.iconbitmap("mouse.ico")
    root.config(bg="black")
    version_info = Label(text=version, padx=10, pady=10, fg="grey", bg="black")
    clicker_status = Label(text="", fg="grey", bg="black")

    start = Label(text="F4 | Start/Stop", bg="black", fg="grey", pady=10, padx=10)

    check = threading.Thread(target=auto_clicker)
    check.start()

    version_info.pack(side=TOP, fill=X)
    clicker_status.pack(fill=X)
    start.pack(side=TOP)
    root.mainloop()


if __name__ == "__main__":
    main()
