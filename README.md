Video Downloader
Introduction

This is a simple video downloader application developed using Python and the Tkinter library. It allows users to download videos from YouTube and Facebook by providing the respective video URLs.
Requirements

    Python 3.x
    tkinter library
    pytube library
    youtube_dl library

Installation

    Ensure Python 3.x is installed on your system.
    Install required libraries using pip:

    pip install pytube youtube_dl

Usage

    Clone or download the provided source code.
    Navigate to the directory containing the code.
    Run the script using Python:

    python video_downloader.py

    The GUI application window will appear.
    Enter the YouTube or Facebook video URL in the respective entry fields.
    Click the "Download YouTube" button to download a YouTube video or the "Download Facebook" button to download a Facebook video.
    After downloading, a message box will appear indicating the success or failure of the download.
    

Code Explanation

    The code imports necessary libraries including tkinter for GUI, messagebox for displaying messages, os for file operations, youtube_dl for downloading YouTube videos, and pytube for downloading Facebook videos.
    Two functions are defined: download_facebook_video(url) and download_youtube_video(url) for downloading videos from Facebook and YouTube, respectively.
    on_entry_click(event, entry) function handles placeholder text and clears the entry field when clicked.
    The Tkinter GUI is created with entry fields for entering video URLs and buttons for initiating downloads.
    The main event loop root.mainloop() runs the application.

Executable

    An executable file named main.exe is provided in the dist folder of the project.
    This executable allows users to run the video downloader application without needing to install Python or any dependencies separately.
    Simply execute the video_downloader.exe file to launch the application.

Notes

    Ensure a stable internet connection is available for downloading videos.
    Videos are downloaded to the Desktop by default.
    Errors are handled using messagebox to notify users of any issues during the download process.
    The provided code and executable are for educational and personal use only.
