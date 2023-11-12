import os
import tkinter
from pytube import YouTube
from tkinter import messagebox

window = tkinter.Tk()
window.minsize(400, 600)
window.title("YouDown")
window.config(bg="aliceblue")


def download():
    url = entry.get()

    if not url:
        messagebox.showerror("Error", message="Please enter a valid URL.")

        return

    path = get_user_download_path()

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        label3.config(text="Downloading your video. Please wait...")
        window.update()

        stream.download(output_path=path)
        label3.config(text="Video has been successfully downloaded.")
        window.update()

    except Exception as e:
        messagebox.showerror("Error", message=f"An error occured: {e}")


def clean():
    entry.delete(0, "end")
    label3.config(text="")


def get_user_download_path():
    if os.name == 'nt':  # Windows
        home_directory = os.path.expanduser("~")
    else:
        home_directory = os.path.expanduser("~" + os.getlogin())

    download_path = os.path.join(home_directory, "Desktop", "YD")

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    return download_path


label = tkinter.Label(text="YOUDOWN\nby rudeboy software", font=("Courier", 20, "bold"), pady=15, padx=30,
                      bg="salmon")
label.pack()

label2 = tkinter.Label(text="Enter the Video URL: ", padx=10, pady=10, font=("Arial", 10, "bold"))
label2.pack()

entry = tkinter.Entry(width=40)
entry.pack()

button = tkinter.Button(text="Download", padx=20, command=download)
button.pack()

label3 = tkinter.Label(pady=10, bg="aliceblue")
label3.pack()

button2 = tkinter.Button(text="Clear", command=clean)
button2.pack()

label4 = tkinter.Label(text="RUDEBOY SOFTWARE\n Copyright: © 2023 etc.", bg="aliceblue", pady=40, padx=40)
label4.pack()

window.mainloop()
