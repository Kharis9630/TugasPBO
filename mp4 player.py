import tkinter as tk
from tkinter import filedialog
import cv2

class VideoPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("MP4 Player")
        self.master.geometry("800x600")

        self.video_path = tk.StringVar()

        self.label = tk.Label(self.master, text="MP4 Player", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.select_button = tk.Button(self.master, text="Select Video", command=self.select_video)
        self.select_button.pack(pady=10)

        self.play_button = tk.Button(self.master, text="Play", command=self.play_video)
        self.play_button.pack(side=tk.LEFT, padx=5)

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_video)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_video)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.volume_label = tk.Label(self.master, text="Volume:")
        self.volume_label.pack(side=tk.LEFT, padx=5)
        
        self.volume_scale = tk.Scale(self.master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.set(50)  # Initial volume set to 50
        self.volume_scale.pack(side=tk.LEFT, padx=5)

        self.cap = None
        self.paused = False

    def select_video(self):
        video_path = filedialog.askopenfilename(initialdir="/", title="Select A Video", filetypes=(("mp4 files", "*.mp4"),))
        if video_path:
            self.video_path.set(video_path)

    def play_video(self):
        if self.cap is not None and not self.paused:
            return

        video_path = self.video_path.get()
        if video_path:
            self.cap = cv2.VideoCapture(video_path)
            self.show_frame()

    def show_frame(self):
        if self.cap is not None:
            ret, frame = self.cap.read()
            if ret:
                # Display the frame here (you can customize this part based on your needs)
                cv2.imshow("Video", frame)

                if not self.paused:
                    self.master.after(10, self.show_frame)

    def pause_video(self):
        self.paused = not self.paused

    def stop_video(self):
        if self.cap is not None:
            self.cap.release()
            cv2.destroyAllWindows()

    def set_volume(self, value):
        volume = int(value) / 100.0
        if self.cap is not None:
            self.cap.set(cv2.CAP_PROP_VOLUME, volume)

if __name__ == "__main__":
    root = tk.Tk()
    video_player = VideoPlayer(root)
    root.mainloop()
