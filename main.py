import tkinter as tk
from tkinter import messagebox
import os
import youtube_dl
from pytube import YouTube


def download_facebook_video(url):
    try:
        # Setting options for youtube_dl
        ydl_opts = {
            'outtmpl': '~/Desktop/%(title)s.%(ext)s'  # Output template for downloaded file
        }

        # Start downloading the video with specified options
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Show a message box after downloading
        messagebox.showinfo("Download Successful", "Video downloaded successfully on the desktop")

    except TypeError as e:
        # Catching TypeError specifically to handle 'NoneType' object error
        messagebox.showerror("Error", f"TypeError: {str(e)}")

    except Exception as e:
        # Catching other exceptions for general error handling
        messagebox.showerror("Error", str(e))


def download_youtube_video(url):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution video stream
        video_stream = yt.streams.get_highest_resolution()

        # Get the path to the desktop directory
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # Download the video to the desktop
        video_stream.download(output_path=desktop_path)

        # Show a message box after downloading
        messagebox.showinfo("Download Successful", "Video downloaded successfully on the desktop")

    except Exception as e:
        # print("An error occurred:", str(e))
        messagebox.showerror("Error", str(e))


def on_entry_click(event, entry):
    if entry.get() == "Enter YouTube URL here" or entry.get() == "Enter Facebook URL here":
        entry.delete(0, tk.END)
        entry.config(fg='black')


root = tk.Tk()
root.title("Download Video")

# Centralizing the GUI
window_width = 600
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create the entry fields with placeholders
entry1 = tk.Entry(root, width=60, fg='grey')
entry1.insert(0, "Enter YouTube URL here")
entry1.bind('<FocusIn>', lambda event, entry=entry1: on_entry_click(event, entry))
entry1.pack(pady=5)

entry2 = tk.Entry(root, width=60, fg='grey')
entry2.insert(0, "Enter Facebook URL here")
entry2.bind('<FocusIn>', lambda event, entry=entry2: on_entry_click(event, entry))
entry2.pack(pady=5)

# Create the buttons
button1 = tk.Button(root, text="Download YouTube", command=lambda: download_youtube_video(entry1.get()))
button1.pack(pady=5)

button2 = tk.Button(root, text="Download Facebook", command=lambda: download_facebook_video(entry2.get()))
button2.pack(pady=5)

root.mainloop()
