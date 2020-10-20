#author test for git on ubuntu
#test 2

import subprocess, os, time
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image
from time import sleep
from shutil import copy

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
				continue

def openAudioFolder():
	subprocess.Popen(f'explorer {os.path.realpath(win_path + folders[0])}')

def openVideoFolder():
	subprocess.Popen(f'explorer {os.path.realpath(win_path + folders[1])}')

def openPlaylistAudioFolder():
	subprocess.Popen(f'explorer {os.path.realpath(win_path + folders[2])}')

def openPlaylistVideoFolder():
	subprocess.Popen(f'explorer {os.path.realpath(win_path + folders[3])}')

def checkUpdates():
	updatepip = subprocess.Popen("python -m pip install --upgrade pip", shell=True)
	subprocess.Popen("pip install --upgrade youtube-dl", shell=True)
	subprocess.Popen("pip install --upgrade Pillow", shell=True)

def checkPATH():
	path_list = os.environ['PATH'].split(';')
	count=0
	for path in path_list:
		if os.path.exists(path + '\\ffmpeg.exe') and os.path.exists(path + '\\ffplay.exe') and os.path.exists(path + '\\ffprobe.exe'):
			print(pathresultsuccess)
			print(path + 'ffmpeg.exe')
			print(path + 'ffplay.exe')
			print(path + 'ffprobe.exe')
			count=0
			break
		elif not os.path.exists(path + '\\ffmpeg.exe') or os.path.exists(path + '\\ffplay.exe') or os.path.exists(path + '\\ffprobe.exe'):
			count += 1
	if count > 0:
		print(pathresultfail)
		for x in path_list:
			print(x)
	else:
		pass

def changeBackgroundImage():
	global bg_image, img_label

	root.filename = filedialog.askopenfilename(initialdir=f"{win_picture_path}", title="File Explorer", filetypes=(("JPEG files", "*.jpeg *.jpg"), ("PNG files", "*.png"), ("All files", "*")))
	actual_file_name = os.path.split(root.filename)

	try:
		with open("images/background.txt", "w") as f:
			if root.filename:
				f.write(actual_file_name[1])
				copy(root.filename, bg_path)
			else:
				f.write("bg1.jpg")

		photo = Image.open(f"{root.filename}")
		new_photo = photo.resize((640,480), Image.ANTIALIAS)
		bg_image = ImageTk.PhotoImage(new_photo)
		img_label = Label(root, image=bg_image, relief=SOLID).place(relwidth=1, relheight=1)
	except:
		pass

	createWindow(root)

def createWindow(root):

	menu = Menu(root) #Create main menu, in which seperate submenus exist
	menu.option_add('*tearOff', False) #Remove ----- in menu

	filemenu = Menu(menu)
	menu.add_cascade(label="File", menu=filemenu)
	filemenu.option_add('*tearOff', False)
	filemenu.add_command(label="Open Audio Folder", command=openAudioFolder)
	filemenu.add_command(label="Open Video Folder", command=openVideoFolder)
	filemenu.add_command(label="Open Playlist Audio Folder", command=openPlaylistAudioFolder)
	filemenu.add_command(label="Open Playlist Video Folder", command=openPlaylistVideoFolder)
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=quitprogram)

	helpmenu = Menu(menu) #Create help dropdown menu
	menu.add_cascade(label="Help", menu=helpmenu) #Add submenu helpmenu to the main menu bar
	helpmenu.option_add('*tearOff', False)
	helpmenu.add_command(label="Check for updates", command=checkUpdates) #Add check for updates box to the help menu
	helpmenu.add_command(label="Check PATH for dependencies", command=checkPATH)
	helpmenu.add_command(label="Change background image", command=changeBackgroundImage)

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

	root.grid_rowconfigure(0, weight=1)#This configures the grid so the 1st and last row are not used, allowing centering in the grid
	root.grid_rowconfigure(5, weight=1)
	root.grid_columnconfigure(0, weight=1)#This configures the grid so the 1st and last column are not used, allowing centering in the grid
	root.grid_columnconfigure(5, weight=1)

	root.title("YouTube-DL-GUI")#Set the title of the window
	root.geometry("640x480") #Set the window width and height
	root.resizable(0,0) #Set the window to be non-resizeable
	root.config(menu=menu)

	root.mainloop()

def downloadAudioHighestQuality():
	#This function only gives you the highest quality audio (aac, flac, mp3, m4a, opus, vorbis, or wav)
	audio_link = audiovar.get()
	link = '"' + str(audio_link) + '"'
	if sys.platform == "win32":
		subprocess.Popen('youtube-dl -i -f bestaudio --extract-audio --no-playlist -o "{}/%(title)s.%(ext)s" {}'.format(win_path + folders[0], link), shell=True).wait()
		audiovar.set("")
	elif sys.platform == "linux":
		subprocess.Popen('youtube-dl -i -f bestaudio --extract-audio --no-playlist -o "{}/%(title)s.%(ext)s" {}'.format(win_path + folders[0], link), shell=True).wait()
		audiovar.set("")
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
		elif sys.platform == "linux":
			subprocess.Popen('youtube-dl -i -f bestvideo+bestaudio/best --no-playlist -o "{}/%(title)s.%(ext)s" {}'.format(win_path + folders[1], link), shell=True).wait()
			videovar.set("")
		else:
			return "Something went wrong."

def downloadPlaylistAudio():
	#This function downloads a playlist as the highest possible audio quality (can be webm, mp4 or mp3/WAV)
	playlistaudio_link = playlistaudiovar.get()
	link = '"' + str(playlistaudio_link) + '"'
	if sys.platform == "win32":
		subprocess.Popen('youtube-dl -i -f bestaudio --extract-audio -o "{}/%(playlist)s/%(title)s.%(ext)s" {}'.format(win_path + folders[2], link), shell=True).wait()
		playlistaudiovar.set("")
	elif sys.platform == "linux":
		subprocess.Popen('youtube-dl -i -f bestaudio --extract-audio -o "{}/%(playlist)s/%(title)s.%(ext)s" {}'.format(win_path + folders[2], link), shell=True).wait()
		playlistaudiovar.set("")
	else:
		return "Something went wrong"   

def downloadPlaylistVideo():
	#This function downloads a playlist as the highest possible video quality (can be webm, mp4 or RAW, mkv)
	playlistvideo_link = playlistvideovar.get()
	link = '"' + str(playlistvideo_link) + '"'
	if sys.platform == "win32":
		subprocess.Popen('youtube-dl -i -f bestvideo+bestaudio/best -o "{}/%(playlist)s/%(title)s.%(ext)s" {}'.format(win_path + folders[3], link), shell=True).wait()
		playlistvideovar.set("")
	elif sys.platform == "linux":
		subprocess.Popen('youtube-dl -i -f bestvideo+bestaudio/best -o "{}/%(playlist)s/%(title)s.%(ext)s" {}'.format(win_path + folders[3], link), shell=True).wait()
		playlistvideovar.set("")
	else:
		return "Something went wrong"
	
def quitprogram():
	root.destroy()

#string variables
user = os.getlogin()
unix_path = "/home/" + user + "/ytdl"
win_path = "C:/Users/" + user + "/ytdl"
folders = ['/audio-hq', '/video-hq', '/playlists-audio', '/playlists-video']
bg_path = "images/"
win_picture_path ="C:/Users/" + user + "/Pictures"
result = "File done downloading."
updatesuccess = "Requirements successfully updated."
pathresultsuccess = "All three ffmpeg packages are in the following PATH."
pathresultfail = "One or more ffmpeg packages are missing in your PATH.\n\
Please ensure you have the following packages and you place them in one of the following folders:\nffmpeg.exe\nffplay.exe\nffprobe.exe\n"

#create folder structure and instantiate Tk object
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
with open("images/background.txt", "r") as f:
	global background_image
	background_image = f.readline()

try:
	bg_image = Image.open(f"images/{background_image}")
	bg_image_2 = bg_image.resize((640, 480), Image.ANTIALIAS)
	bg_image_resized = ImageTk.PhotoImage(bg_image_2)
	img_label = Label(root, image=bg_image_resized, relief=SOLID).place(relwidth=1, relheight=1)
except:
	try:
		bg_image = Image.open(f"images/bg1.jpg")
		bg_image_2 = bg_image.resize((640, 480), Image.ANTIALIAS)
		bg_image_resized = ImageTk.PhotoImage(bg_image_2)
		img_label = Label(root, image=bg_image_resized, relief=SOLID).place(relwidth=1, relheight=1)
	except:
		print("Please place an image named bg1.jpg into the images folder if you encounter further issues.")

createWindow(root)
