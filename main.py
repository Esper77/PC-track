from tkinter import *
from PIL import Image, ImageTk
import psutil


window = Tk()
window.title("Load")


cpu = StringVar()
mem = StringVar()
disk = StringVar()


def iteration():
    global cpu
    cpu.set("CPU load:" + str(psutil.cpu_percent()) + '%')
    global mem
    mem.set("Memory load:" + str(psutil.virtual_memory().percent) + '%')
    global disk
    disk.set("Disk usage:" + str(psutil.disk_usage("/").used // 1000000000) + 'GB /' + str(psutil.disk_usage("/").total // 1000000000) +
          'GB')
    window.after(1000, iteration)


img_cpu = ImageTk.PhotoImage(Image.open("cpu.png"))
img_mem = ImageTk.PhotoImage(Image.open("ram.png"))
img_disk = ImageTk.PhotoImage(Image.open("disk.png"))


Label(window, image=img_cpu).grid(row=0, column=0)
Label(window, image=img_mem).grid(row=1, column=0)
Label(window, image=img_disk).grid(row=2, column=0)
Label(window, textvariable=cpu).grid(row=0, column=1)
Label(window, textvariable=mem).grid(row=1, column=1)
Label(window, textvariable=disk).grid(row=2, column=1)

iteration()

mainloop()
