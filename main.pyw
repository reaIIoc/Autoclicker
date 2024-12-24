# Autoclicker built with tkinter and pyautogui.

import tkinter
from tkinter import *
import pydirectinput
import time
import threading
import win32api


version = "Autoclicker 1.0.1 | Maintained by datarec"
status = False
clicks_interval = 0
clicks_config = 0
cc_count = 0
ic_count = 0


def read_config():
    global ic_count
    global cc_count
    global clicks_config
    global clicks_interval
    with open("autoclicker.cfg", "r") as click_r:
        for cclick in click_r:
            setting = str(cclick).strip("click_interval clicks_per_interval =")
            if cc_count == 1:
                clicks_interval = setting
            cc_count += 1
    with open("autoclicker.cfg", "r") as click_i:
        for iclick in click_i:
            isetting = str(iclick).strip("click_interval clicks_per_interval =")
            if ic_count == 2:
                clicks_config = isetting
            ic_count += 1
            


def auto_clicker():
    read_config()
    global status
    while True:
        parent = threading.main_thread()
        parent_status = str(parent).split(",")[1]
        key_press = win32api.GetKeyState(0x73)
        status = key_press
        if status == 0:
            pass
        elif "stopped" in parent_status:
            print("yay")
            quit()
        elif status == 1:
            #i_clicks_interval = int(clicks_interval)
            i_clicks_config = int(clicks_config) 
            pydirectinput.click(button="left", interval=0, clicks=i_clicks_config)


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
