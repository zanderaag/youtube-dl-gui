
import os, sys

#use r to denote a rawstring so windows paths with \ do not get treated as unicode characters and error out
r'''
youtube-dl downloader app needs to do the following:
1.[] Download audio at various qualities.
    -MP3
    -WAV
2.[] Download video at various qualities.
    -RAW (4K)
    -MP4
    -WEBM
3.[x] Download audio and video from a video seperately in various qualities.
4.[x] Download playlist(s) at various qualities.
    -Each playlist should be stored in its own named folder under the playlists/ directory.
    -Option to download playlist as all audio (best quality), or video (best quality).
5.[x] Format video/song titles to remove clutter/gibberish.
6.[x] Check if destination folder(s) for audio/video/streams/playlists exists, if not create them. Ignoring config file as this is more intuitive.
    -Windows
    -Linux
7.[] Check for updates to youtube-dl, ffmpeg
8.[] Ensure that the ffmpeg, ffprobe, and ffplay executables ALONG with youtube-dl.exe are in your PATH.

Currently the only way to convert video to audio is with ffmpeg, ffprobe and ffplay.
Using 'pip install ffmpeg/ffprobe' does not work because it cannot find the ffmpeg/ffprobe/ffplay executables.
Manually downloading ffmpeg/ffprobe and placing it into your C:\Users\$USERNAME\AppData\Local\Programs\Python\Python38\Scripts folder does the job though.
Any folder in your PATH will work also, however since the youtube-dl.exe is in there already, i figured those should be too.
'''

#Variables
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
               continue

    elif sys.platform == "linux":
        #Create root folder to store all your respective file type folders: /home/$user/ytdl
        if os.path.isdir(unix_path):
            pass
        else:
            os.mkdir(unix_path)

        for fol in folders:
            if not os.path.exists(unix_path + fol):
                os.mkdir(unix_path + fol)
                print("{}{} has been created".format(unix_path, fol))
            else:
                continue   

def downloadAudioHighestQuality(audio_link):
    #This function only gives you the highest quality audio (aac, flac, mp3, m4a, opus, vorbis, or wav)
    link = '"' + str(audio_link) + '"'
    if sys.platform == "win32":
        os.system('youtube-dl -i -f bestaudio --extract-audio --no-playlist -o "{}/%(title)s.%(ext)s" {}'.format(win_path + folders[0], link))
    elif sys.platform == "linux":
        os.system('youtube-dl -i -f bestaudio --extract-audio --no-playlist -o "{}/%(title)s.%(ext)s" {}'.format(unix_path + folders[0], link))
    else:
        return "Something went wrong."

def downloadVideoHighestQuality(video_link):
    #This function gives you the highest quality video and audio seperately merged into a single file
    #If best formats are not compatible with eachother it will merge into a .mkv
    link = '"' + str(video_link) + '"'
    if "playlist" in link:
        print("Invalid URL. Please do not supply this function with a direct playlist link.")
        return 0
    else:
        if sys.platform == "win32":
            os.system('youtube-dl -i -f bestvideo+bestaudio/best --no-playlist -o "{}/%(title)s.%(ext)s" {}'.format(win_path + folders[1], link))
        elif sys.platform == "linux":
            os.system('youtube-dl -i -f bestvideo+bestaudio/best --no-playlist -o "{}/%(title)s.%(ext)s" {}'.format(unix_path + folders[1], link))
        else:
            return "Something went wrong."

def downloadMP3(audio_link):
    #This function downloads the audio at its highest quality and converts it to MP3
    link = '"' + str(audio_link) + '"'
    if sys.platform == "win32":
        os.system('youtube-dl -i -f bestaudio --no-playlist --extract-audio --audio-format mp3 --audio-quality 0 -o "{}/%(title)s.%(ext)s" {}'.format(win_path + folders[5], link))
    elif sys.platform == "linux":
        os.system('youtube-dl -i -f bestaudio --no-playlist --extract-audio --audio-format mp3 --audio-quality 0 -o "{}/%(title)s.%(ext)s" {}'.format(unix_path + folders[5], link))
    else:
        return "Something went wrong."

def downloadWAV(audio_link):
    #This function downloads the audio at its highest quality and converts it to WAV
    link = '"' + str(audio_link) + '"'
    if sys.platform == "win32":
        os.system('youtube-dl -i -f bestaudio --no-playlist --extract-audio --audio-format wav --audio-quality 0 -o "{}/%(title)s.%(ext)s" {}'.format(win_path + folders[6], link))
    elif sys.platform == "linux":
        os.system('youtube-dl -i -f bestaudio --no-playlist --extract-audio --audio-format wav --audio-quality 0 -o "{}/%(title)s.%(ext)s" {}'.format(unix_path + folders[6], link))
    else:
        return "Something went wrong."

def downloadPlaylistAudio(playlist_link):
    #This function downloads a playlist as the highest possible audio quality (can be webm, mp4 or mp3/WAV)
    link = '"' + str(playlist_link) + '"'
    if sys.platform == "win32":
        os.system('youtube-dl -i -f bestaudio --extract-audio -o "{}/%(playlist)s/%(title)s.%(ext)s" {}'.format(win_path + folders[2], link))
    elif sys.platform == "linux":
        os.system('youtube-dl -i -f bestaudio --extract-audio -o "{}/%(playlist)s/%(title)s.%(ext)s" {}'.format(unix_path + folders[2], link))
    else:
        return "Something went wrong"   

def downloadPlaylistVideo(playlist_link):
    #This function downloads a playlist as the highest possible video quality (can be webm, mp4 or RAW, mkv)
    link = '"' + str(playlist_link) + '"'
    if sys.platform == "win32":
        os.system('youtube-dl -i -f bestvideo+bestaudio/best -o "{}/%(playlist)s/%(title)s.%(ext)s" {}'.format(win_path + folders[3], link))
    elif sys.platform == "linux":
        os.system('youtube-dl -i -f bestvideo+bestaudio/best -o "{}/%(playlist)s/%(title)s.%(ext)s" {}'.format(unix_path + folders[3], link))
    else:
        return "Something went wrong"

def print_menu():       
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Download Audio (HQ)")
    print("2. Download Video (HQ)")
    print("3. Download MP3")
    print("4. Download WAV")
    print("5. Download Playlist Audio (HQ)")
    print("6. Download Playlist Video (HQ)")
    print("0. Exit")
    print(67 * "-")

if __name__ == "__main__":

    print_menu()

    createFolderStructure()

    loop=True      

    while loop:
        try:
            os.system('cls')
        except:
            os.system('clear')

        print_menu() 
        choice = input("Enter your choice [1-5]: ")
        
        if choice == '1':     
            link = input(str("Enter URL: "))
            downloadAudioHighestQuality(link)

        elif choice == '2':
            link = input(str("Enter URL: "))
            downloadVideoHighestQuality(link)    

        elif choice == '3':
            link = input(str("Enter URL: "))
            downloadMP3(link)
            
        elif choice == '4':
            link = input(str("Enter URL: "))
            downloadWAV(link)
            
        elif choice == '5':
            link = input(str("Enter URL: "))
            downloadPlaylistAudio(link)
            
        elif choice == '6':
            link = input(str("Enter URL: "))
            downloadPlaylistVideo(link)

        elif choice == '0':
            loop = False 

        else:
            input("Wrong option selection. Enter any key to try again..")


