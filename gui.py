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
# root.geometry("250x250") #Set the window width and height
root.resizable(0,0) #Set the window to be non-resizeable

download_button_image = Image.open("images/download_button.png")
download_button_resize = download_button_image.resize((15,15), Image.ANTIALIAS)
download_button_tk = ImageTk.PhotoImage(download_button_resize)


label1 = Label(root, text="Audio")
entry1 = Entry(root)
button1 = Button(root, image=download_button_tk)

label2 = Label(root, text="Video")
entry2 = Entry(root)
button2 = Button(root, image=download_button_tk)

label3 = Label(root, text="Playlist Audio")
entry3 = Entry(root)
button3 = Button(root, image=download_button_tk)

label4 = Label(root, text="Playlist Video")
entry4 = Entry(root)
button4 = Button(root, image=download_button_tk)

label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)
label3.grid(row=2, sticky=E)
label4.grid(row=3, sticky=E)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)

button1.grid(row=0, column=2)
button2.grid(row=1, column=2)
button3.grid(row=2, column=2)
button4.grid(row=3, column=2)

root.mainloop()