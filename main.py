from pytube import YouTube
from tkinter import *
from os import startfile
import webbrowser
import pathlib


def download_video():
    link = link_input.get()
    download_video.video = YouTube(link)

    vid_download = download_video.video.streams.get_highest_resolution()
    vid_download.download("downloads")
    print("\"" + download_video.video.title + "\"" + "downloaded")


def play_video():
    if '.' in download_video.video.title:
        fixed_download = download_video.video.title.replace('.',"")
        video_file = (fixed_download + ".mp4")
    else:
        video_file = (download_video.video.title + ".mp4")

    startfile("downloads\\" + video_file)


def open_downloads():
    path = pathlib.Path(__file__).parent.resolve()
    webbrowser.open("file:///" + str(path) + "\\downloads")


window = Tk()
window.title("YouTube Downloader")
window.geometry("500x200")

link_label = Label(window, text="Link: ")
link_label.grid(row=1, column=0)

link_input = Entry(window, width=75)
link_input.grid(row=1, column=1)

download_button = Button(window, text="Begin download", command=download_video)
download_button.grid(row=2, column=1)

play_button = Button(window, text="Click here to play downloaded video", command=play_video)
play_button.grid(row=3, column=1)

open_folder_button = Button(window, text="Click here to open downloads folder", command=open_downloads)
open_folder_button.grid(row=4, column=1)

window.mainloop()

