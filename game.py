import os
import time
import tkinter as tk



def play_song_button_clicked1():
    song_name = song_entry.get()
    if song_name == "שבט צופים אחים ואחיות":
        message_label.configure(text="Congratulations!", fg="green", font=("Helvetica", 30))
        time.sleep(3)
        os.startfile("TRIBE.mp3")
    else:
        print("Error: Invalid song name")


def play_song_button_clicked2():
    song_name = song_entry.get()
    if song_name == "מדעי המחשב ללא מחשב":
        message_label.configure(text="Congratulations!", fg="green", font=("Helvetica", 30))
        time.sleep(3)
        os.startfile("NOAH.mp3")
    else:
        print("Error: Invalid song name")


root = tk.Tk()
root.geometry("500x300")
root.title("ENIGMA")

song_label = tk.Label(text="Enter the password for any song:")
song_label.pack()

song_entry = tk.Entry()
song_entry.pack()

song_label = tk.Label(text="")
song_label.pack()

song_label = tk.Label(text="")
song_label.pack()
message_label = tk.Label(text="(3,9,40,20,4,9)  - (70,40,20,4) -  (70,40,200,9,300) - (30,5,2)", font=("Helvetica", 10))
message_label.pack()
play_song_button1 = tk.Button(text="Play Song 1", command=play_song_button_clicked1)
play_song_button1.pack()

song_label = tk.Label(text="")
song_label.pack()

song_label = tk.Label(text="")
song_label.pack()
message_label = tk.Label(text="{8,6,70,400} - {20,1,2} - {60,40,1,7,400} - {6,40,2,30}", font=("Helvetica", 10))
message_label.pack()
play_song_button2 = tk.Button(text="Play Song 2", command=play_song_button_clicked2)
play_song_button2.pack()

root.mainloop()
