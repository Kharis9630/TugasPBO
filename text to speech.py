import tkinter as tk
from tkinter import scrolledtext
import pyttsx3

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Text to Speech")
        self.master.geometry("400x300")

        self.text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack(pady=10)

        self.speak_button = tk.Button(self.master, text="Speak", command=self.speak_text)
        self.speak_button.pack(pady=5)

        self.engine = pyttsx3.init()

    def speak_text(self):
        text_to_speak = self.text_area.get("1.0", tk.END).strip()
        if text_to_speak:
            self.engine.say(text_to_speak)
            self.engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
