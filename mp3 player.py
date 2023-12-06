import os
import pygame
from tkinter import Tk, Listbox, Button, filedialog, END, SINGLE  # Add SINGLE here

class MP3Player:
    def __init__(self, master):
        self.master = master
        self.master.title("MP3 Player")
        self.master.geometry("400x500")

        self.playlist = Listbox(self.master, selectmode=SINGLE, bg="lightblue", selectbackground="gray")
        self.playlist.pack(pady=10)

        self.play_button = Button(self.master, text="Play", command=self.play)
        self.play_button.pack(pady=5)

        self.pause_button = Button(self.master, text="Pause", command=self.pause)
        self.pause_button.pack(pady=5)

        self.stop_button = Button(self.master, text="Stop", command=self.stop)
        self.stop_button.pack(pady=5)

        self.add_button = Button(self.master, text="Add Song", command=self.add_song)
        self.add_button.pack(pady=5)

        self.song_list = []
        self.paused = False
        self.pause_position = 0

    def add_song(self):
        song = filedialog.askopenfilename(initialdir="/", title="Select A Song", filetypes=(("mp3 files", "*.mp3"),))
        if song:
            self.song_list.append(song)
            self.playlist.insert(END, os.path.basename(song))

    def play(self):
        if self.song_list:
            selected_song_index = self.playlist.curselection()
            selected_song = self.song_list[selected_song_index[0]]
            
            if not self.paused:
                pygame.mixer.init()
                pygame.mixer.music.load(selected_song)
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.unpause()
                self.paused = False

    def pause(self):
        if pygame.mixer.music.get_busy() and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
            self.pause_position = pygame.mixer.music.get_pos()

    def stop(self):
        pygame.mixer.music.stop()
        self.paused = False

if __name__ == "__main__":
    root = Tk()
    mp3_player = MP3Player(root)
    root.mainloop()
