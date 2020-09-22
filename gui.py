
from ytdl import *
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import subprocess


'''
1. Make GUI buttons corresponding to each function, and when the button is pressed a box will appear for you to paste your link into it.
   Once the link is pasted, you press a button (or press enter) and the box will give you a loading bar of your progress before showing "Success" or "Failure" and exiting out.
2. Make button to check for/download dependencies (youtube-dl, ffmpeg) and check they are in PATH
3. Make a button to open your download folders in Windows Explorer
'''

#First step of a tkinter gui is creating the window and the size/positioning

#The variables inside these four functions are imported from ytdl.py
def openAudioFolder():
    if sys.platform == "win32":
        subprocess.Popen(f'explorer {os.path.realpath(win_path + folders[0])}')
    elif sys.platform == "linux":
        subprocess.Popen(f'explorer {os.path.realpath(unix_path + folders[0])}')

def openVideoFolder():
    if sys.platform == "win32":
        subprocess.Popen(f'explorer {os.path.realpath(win_path + folders[1])}')
    elif sys.platform == "linux":
        subprocess.Popen(f'explorer {os.path.realpath(unix_path + folders[1])}')

def openPlaylistAudioFolder():
    if sys.platform == "win32":
        subprocess.Popen(f'explorer {os.path.realpath(win_path + folders[2])}')
    elif sys.platform == "linux":
        subprocess.Popen(f'explorer {os.path.realpath(unix_path + folders[2])}')

def openPlaylistVideoFolder():
    if sys.platform == "win32":
        subprocess.Popen(f'explorer {os.path.realpath(win_path + folders[3])}')
    elif sys.platform == "linux":
        subprocess.Popen(f'explorer {os.path.realpath(unix_path + folders[3])}')

def quitprogram():
    root.destroy()

root = Tk()

download_button_image = Image.open("images/download_button.png")
download_button_resize = download_button_image.resize((15,15), Image.ANTIALIAS)
download_button_tk = ImageTk.PhotoImage(download_button_resize)

menu = Menu(root) #create main menu, in which seperate submenus exist
menu.option_add('*tearOff', False) #remove ----- in menu

filemenu = Menu(menu)
filemenu.option_add('*tearOff', False)
filemenu.add_command(label="Open Audio Folder", command=openAudioFolder)
filemenu.add_command(label="Open Video Folder", command=openVideoFolder)
filemenu.add_command(label="Open Playlist Audio Folder", command=openPlaylistAudioFolder)
filemenu.add_command(label="Open Playlist Video Folder", command=openPlaylistVideoFolder)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quitprogram)
menu.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menu) #create help dropdown menu
helpmenu.option_add('*tearOff', False)
helpmenu.add_command(label="About me")
helpmenu.add_command(label="License")
helpmenu.add_command(label="Check for updates") #add check for updates box to the help menu
menu.add_cascade(label="Help", menu=helpmenu) #add submenu helpmenu to the main menu bar

bg_image = PhotoImage(file="images/fuckconverters.png")
img_label = Label(root, image=bg_image).place(relwidth=1, relheight=1)

label1 = Label(root, text="Audio").grid(row=1, sticky="E")
entry1 = Entry(root, width=70).grid(row=1, column=1)
button1 = Button(root, image=download_button_tk).grid(row=1, column=2)

label2 = Label(root, text="Video").grid(row=2, sticky="E")
entry2 = Entry(root, width=70).grid(row=2, column=1)
button2 = Button(root, image=download_button_tk).grid(row=2, column=2)

label3 = Label(root, text="Playlist Audio").grid(row=3, sticky="E")
entry3 = Entry(root, width=70).grid(row=3, column=1)
button3 = Button(root, image=download_button_tk).grid(row=3, column=2)

label4 = Label(root, text="Playlist Video").grid(row=4, sticky="E")
entry4 = Entry(root, width=70).grid(row=4, column=1)
button4 = Button(root, image=download_button_tk).grid(row=4, column=2)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(5, weight=1)

root.title("ytdl-gui")
root.geometry("552x500") #Set the window width and height
root.resizable(0,0) #Set the window to be non-resizeable
root.config(menu=menu)

root.mainloop()

