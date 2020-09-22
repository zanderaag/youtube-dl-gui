
from ytdl import *
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

'''
1. Make GUI buttons corresponding to each function, and when the button is pressed a box will appear for you to paste your link into it.
   Once the link is pasted, you press a button (or press enter) and the box will give you a loading bar of your progress before showing "Success" or "Failure" and exiting out.
2. Make button to check for/download dependencies (youtube-dl, ffmpeg) and check they are in PATH
3. Make a button to open your download folders in Windows Explorer
'''

#First step of a tkinter gui is creating the window and the size/positioning

def printName():
    print("name")

root = Tk()
root.title("ytdl-gui")
root.geometry("700x633") #Set the window width and height
root.resizable(0,0) #Set the window to be non-resizeable

download_button_image = Image.open("images/download_button.png")
download_button_resize = download_button_image.resize((15,15), Image.ANTIALIAS)
download_button_tk = ImageTk.PhotoImage(download_button_resize)

bg_image = PhotoImage(file="images/fuckspotify.png")
img_label = Label(root, image=bg_image).place(relwidth=1, relheight=1)

label1 = Label(root, text="Audio").grid(row=1, sticky="E")
entry1 = Entry(root).grid(row=1, column=1)
button1 = Button(root, image=download_button_tk).grid(row=1, column=2)

label2 = Label(root, text="Video").grid(row=2, sticky="E")
entry2 = Entry(root).grid(row=2, column=1)
button2 = Button(root, image=download_button_tk).grid(row=2, column=2)

label3 = Label(root, text="Playlist Audio").grid(row=3, sticky="E")
entry3 = Entry(root).grid(row=3, column=1)
button3 = Button(root, image=download_button_tk).grid(row=3, column=2)

label4 = Label(root, text="Playlist Video").grid(row=4, sticky="E")
entry4 = Entry(root).grid(row=4, column=1)
button4 = Button(root, image=download_button_tk).grid(row=4, column=2)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(5, weight=1)

root.mainloop()

