# from ytdl import *
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image
import subprocess, os, time
from time import sleep

'''
1. Make GUI buttons corresponding to each function, and when the button is pressed a box will appear for you to paste your link into it.
   Once the link is pasted, you press a button (or press enter) and the box will give you a loading bar of your progress before showing "Success" or "Failure" and exiting out.
2. Make button to check for/download dependencies (youtube-dl, ffmpeg) and check they are in PATH
3. Make a button to open your download folders in Windows Explorer
'''

result = "File done downloading."
pathresultsuccess = "All three ffmpeg packages are in the PATH."
pathresultfail = "One or more ffmpeg packages are missing in your PATH.\n\
Please ensure you have the following packages:\nffmpeg.exe\nffplay.exe\nffprobe.exe"
updatesuccess = "Requirements successfully updated."

user = os.getlogin()
unix_path = "/home/" + user + "/ytdl"
win_path = "C:/Users/" + user + "/ytdl"
folders = ['/audio-hq', '/video-hq', '/playlists-audio', '/playlists-video', '/streams', '/mp3', '/wav']

def createFolderStructure():
	if sys.platform == "win32":
		#Create root folder to store all your respective file type folders: C:/Users/$USERNAME/ytdl
		if os.path.isdir(win_path):
			pass
		else:
			os.mkdir(win_path)

		for fol in folders:
			if not os.path.exists(win_path + fol):
				os.mkdir(win_path + fol)
				print("{}{} has been created".format(win_path, fol))
			else:
				# print(f"Sub folder {win_path + fol} present. Continuing...")
				continue

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

def checkUpdates():
	updatepip = subprocess.Popen("python -m pip install --upgrade pip", shell=True)
	subprocess.Popen("pip install --upgrade youtube-dl", shell=True)
	subprocess.Popen("pip install --upgrade Pillow", shell=True)
	sleep(3)
	showCompletedDownloadWindow(updatesuccess)

def checkPATH():
	path_list = os.environ['PATH'].split(';') 
	for path in path_list:
		if os.path.exists(path + 'ffmpeg.exe') and os.path.exists(path + 'ffplay.exe') and os.path.exists(path + 'ffprobe.exe'):
			showCompletedDownloadWindow(pathresultsuccess)
		elif not os.path.exists(path + 'ffmpeg.exe') and os.path.exists(path + 'ffplay.exe') and os.path.exists(path + 'ffprobe.exe'):
			showCompletedDownloadWindow(pathresultfail)

def changeBackgroundImage():
	global bg_image, img_label
	root.filename = filedialog.askopenfilename(initialdir=f"{win_path + 'Pictures'}", title="File Explorer", filetypes=(("JPEG files", "*.jpeg *.jpg"), ("PNG files", "*.png"), ("All files", "*")))
	photo = Image.open(f"{root.filename}")
	new_photo = photo.resize((640,480), Image.ANTIALIAS)
	bg_image = ImageTk.PhotoImage(new_photo)
	img_label = Label(root, image=bg_image, relief=SOLID).place(relwidth=1, relheight=1)

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
	helpmenu.add_command(label="Check for updates", command=checkUpdates) #add check for updates box to the help menu
	helpmenu.add_command(label="Check PATH for dependencies", command=checkPATH)
	helpmenu.add_command(label="Change background image", command=changeBackgroundImage)
	menu.add_cascade(label="Help", menu=helpmenu) #add submenu helpmenu to the main menu bar

	label1 = Label(root, text="Audio").grid(row=1, sticky="E")
	entry1 = Entry(root, width=70, textvariable=audiovar).grid(row=1, column=1)
	button1 = Button(root, image=download_button_tk, command=lambda: downloadAudioHighestQuality()).grid(row=1, column=2)

	label2 = Label(root, text="Video").grid(row=2, sticky="E")
	entry2 = Entry(root, width=70, textvariable=videovar).grid(row=2, column=1)
	button2 = Button(root, image=download_button_tk, command=lambda: downloadVideoHighestQuality()).grid(row=2, column=2)

	label3 = Label(root, text="Playlist Audio").grid(row=3, sticky="E")
	entry3 = Entry(root, width=70, textvariable=playlistaudiovar).grid(row=3, column=1)
	button3 = Button(root, image=download_button_tk, command=lambda: downloadPlaylistAudio()).grid(row=3, column=2)

	label4 = Label(root, text="Playlist Video").grid(row=4, sticky="E")
	entry4 = Entry(root, width=70, textvariable=playlistvideovar).grid(row=4, column=1)
	button4 = Button(root, image=download_button_tk, command=lambda: downloadPlaylistVideo()).grid(row=4, column=2)

	root.grid_rowconfigure(0, weight=1)
	root.grid_rowconfigure(5, weight=1)
	root.grid_columnconfigure(0, weight=1)
	root.grid_columnconfigure(5, weight=1)

	root.title("YouTube-DL-GUI")
	root.geometry("640x480") #Set the window width and height
	root.resizable(0,0) #Set the window to be non-resizeable
	root.config(menu=menu)

	root.mainloop()

def showCompletedDownloadWindow(output):
	if output == result:
		newWindow = Toplevel(root)
		newWindow.geometry('180x50')
		dltext = Text(newWindow, wrap=WORD)
		dltext.insert(END, result)
		dltext.config(state=DISABLED)
		dltext.grid(row=1, column=1)
	elif output == pathresultsuccess:
		newWindow = Toplevel(root)
		newWindow.geometry('340x50')
		dltext = Text(newWindow, wrap=WORD)
		dltext.insert(END, pathresultsuccess)
		dltext.config(state=DISABLED)
		dltext.grid(row=1, column=1)
	elif output == pathresultfail:
		newWindow = Toplevel(root)
		newWindow.geometry('420x90')
		dltext = Text(newWindow, wrap=WORD)
		dltext.insert(END, pathresultfail)
		dltext.config(state=DISABLED)
		dltext.grid(row=1, column=1)
	elif output == updatesuccess:
		newWindow = Toplevel(root)
		newWindow.geometry('420x90')
		dltext = Text(newWindow, wrap=WORD)
		dltext.insert(END, updatesuccess)
		dltext.config(state=DISABLED)
		dltext.grid(row=1, column=1)

def downloadAudioHighestQuality():
	#This function only gives you the highest quality audio (aac, flac, mp3, m4a, opus, vorbis, or wav)
	audio_link = audiovar.get()
	link = '"' + str(audio_link) + '"'
	if sys.platform == "win32":
		subprocess.Popen('youtube-dl -i -f bestaudio --extract-audio --no-playlist -o "{}/%(title)s.%(ext)s" {}'.format(win_path + folders[0], link), shell=True).wait()
		audiovar.set("")
		# showCompletedDownloadWindow(result)
	elif sys.platform == "linux":
		subprocess.Popen('youtube-dl -i -f bestaudio --extract-audio --no-playlist -o "{}/%(title)s.%(ext)s" {}'.format(win_path + folders[0], link), shell=True).wait()
		audiovar.set("")
		# showCompletedDownloadWindow(result)
	else:
		audiovar.set("")
		return "Something went wrong."

def downloadVideoHighestQuality():
	#This function gives you the highest quality video and audio seperately merged into a single file
	#If best formats are not compatible with eachother it will merge into a .mkv
	video_link = videovar.get()
	link = '"' + str(video_link) + '"'
	if "playlist" in link:
		print("Invalid URL. Please do not supply this function with a direct playlist link.")
		return 0
	else:
		if sys.platform == "win32":
			subprocess.Popen('youtube-dl -i -f bestvideo+bestaudio/best --no-playlist -o "{}/%(title)s.%(ext)s" {}'.format(win_path + folders[1], link), shell=True).wait()
			videovar.set("")
			# showCompletedDownloadWindow(result)
		elif sys.platform == "linux":
			subprocess.Popen('youtube-dl -i -f bestvideo+bestaudio/best --no-playlist -o "{}/%(title)s.%(ext)s" {}'.format(win_path + folders[1], link), shell=True).wait()
			videovar.set("")
			# showCompletedDownloadWindow(result)
		else:
			return "Something went wrong."

def downloadPlaylistAudio():
	#This function downloads a playlist as the highest possible audio quality (can be webm, mp4 or mp3/WAV)
	playlistaudio_link = playlistaudiovar.get()
	link = '"' + str(playlistaudio_link) + '"'
	if sys.platform == "win32":
		subprocess.Popen('youtube-dl -i -f bestaudio --extract-audio -o "{}/%(playlist)s/%(title)s.%(ext)s" {}'.format(win_path + folders[2], link), shell=True).wait()
		playlistaudiovar.set("")
		# showCompletedDownloadWindow(result)
	elif sys.platform == "linux":
		subprocess.Popen('youtube-dl -i -f bestaudio --extract-audio -o "{}/%(playlist)s/%(title)s.%(ext)s" {}'.format(win_path + folders[2], link), shell=True).wait()
		playlistaudiovar.set("")
		# showCompletedDownloadWindow(result)
	else:
		return "Something went wrong"   

def downloadPlaylistVideo():
	#This function downloads a playlist as the highest possible video quality (can be webm, mp4 or RAW, mkv)
	playlistvideo_link = playlistvideovar.get()
	link = '"' + str(playlistvideo_link) + '"'
	if sys.platform == "win32":
		subprocess.Popen('youtube-dl -i -f bestvideo+bestaudio/best -o "{}/%(playlist)s/%(title)s.%(ext)s" {}'.format(win_path + folders[3], link), shell=True).wait()
		playlistvideovar.set("")
		# showCompletedDownloadWindow(result)
	elif sys.platform == "linux":
		subprocess.Popen('youtube-dl -i -f bestvideo+bestaudio/best -o "{}/%(playlist)s/%(title)s.%(ext)s" {}'.format(win_path + folders[3], link), shell=True).wait()
		playlistvideovar.set("")
		# showCompletedDownloadWindow(result)
	else:
		return "Something went wrong"
	
def quitprogram():
	root.destroy()

createFolderStructure()

root = Tk()

#variables for the Entry objects
videovar = StringVar()
audiovar = StringVar()
playlistaudiovar = StringVar()
playlistvideovar = StringVar()

#download button code
download_button_image = Image.open("images/download_button.png")
download_button_resize = download_button_image.resize((15,15), Image.ANTIALIAS)
download_button_tk = ImageTk.PhotoImage(download_button_resize)

#initial background image code
bg_image = Image.open("images/bg1.jpg")
bg_image_2 = bg_image.resize((640, 480), Image.ANTIALIAS)
bg_image_resized = ImageTk.PhotoImage(bg_image_2)
img_label = Label(root, image=bg_image_resized, relief=SOLID).place(relwidth=1, relheight=1)

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
helpmenu.add_command(label="Check for updates", command=checkUpdates) #add check for updates box to the help menu
helpmenu.add_command(label="Check PATH for dependencies", command=checkPATH)
helpmenu.add_command(label="Change background image", command=changeBackgroundImage)
menu.add_cascade(label="Help", menu=helpmenu) #add submenu helpmenu to the main menu bar

label1 = Label(root, text="Audio").grid(row=1, sticky="E")
entry1 = Entry(root, width=70, textvariable=audiovar).grid(row=1, column=1)
button1 = Button(root, image=download_button_tk, command=lambda: downloadAudioHighestQuality()).grid(row=1, column=2)

label2 = Label(root, text="Video").grid(row=2, sticky="E")
entry2 = Entry(root, width=70, textvariable=videovar).grid(row=2, column=1)
button2 = Button(root, image=download_button_tk, command=lambda: downloadVideoHighestQuality()).grid(row=2, column=2)

label3 = Label(root, text="Playlist Audio").grid(row=3, sticky="E")
entry3 = Entry(root, width=70, textvariable=playlistaudiovar).grid(row=3, column=1)
button3 = Button(root, image=download_button_tk, command=lambda: downloadPlaylistAudio()).grid(row=3, column=2)

label4 = Label(root, text="Playlist Video").grid(row=4, sticky="E")
entry4 = Entry(root, width=70, textvariable=playlistvideovar).grid(row=4, column=1)
button4 = Button(root, image=download_button_tk, command=lambda: downloadPlaylistVideo()).grid(row=4, column=2)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(5, weight=1)

root.title("YouTube-DL-GUI")
root.geometry("640x480") #Set the window width and height
root.resizable(0,0) #Set the window to be non-resizeable
root.config(menu=menu)

root.mainloop()

