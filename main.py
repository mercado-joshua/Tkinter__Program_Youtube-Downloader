#===========================
# Imports
#===========================
import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd, simpledialog as sd

import pafy
# pip install youtube_dl
import pyperclip
import os

#===========================
# Main App
#===========================
class App(tk.Tk):
    """Main Application."""
    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_widgets()

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.resizable(True, True)
        self.title('Youtube Downloader Version 1.0')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def init_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        fieldset = ttk.LabelFrame(frame, text='Download Youtube Video')
        fieldset.pack(side=tk.TOP, expand=True, padx=10, pady=10, fill=tk.BOTH)

        label = ttk.Label(fieldset, text='Video URL *copy the video link first')
        label.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10, pady=(10, 0))

        self.query = tk.StringVar()
        self.query.set(pyperclip.paste())
        entry = ttk.Entry(fieldset, width=80, textvariable=self.query)
        entry.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10)

        self.button = ttk.Button(fieldset, text='Download', command=self.download)
        self.button.pack(side=tk.RIGHT, anchor=tk.W, padx=(0, 10), pady=10)

    # ------------------------------------------
    def download(self):
        self.button.config(state=tk.DISABLED)
        video = pafy.new(self.query.get())

        print(video.title)
        # print rating
        print(video.rating)
        # print viewcount
        print(video.viewcount)
        # print author
        print(video.author)
        # print duration
        print(video.duration)
        # print likes
        print(video.likes)
        # print dislikes
        print(video.dislikes)

        # possible resolution available
        streams = video.streams
        for i in streams:
            print(i)

        # get best resolution regardless of format
        best = video.getbest()
        print(best.resolution, best.extension)
        # download the video
        best.download()

        self.button.config(state=tk.NORMAL)

        os.startfile(f'{video.title}.mp4')

#===========================
# Start GUI
#===========================
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()