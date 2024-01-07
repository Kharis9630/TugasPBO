import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class TextExtractorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Extractor")
        self.master.geometry("600x400")
        self.master.configure(bg="teal")

        self.image_path = tk.StringVar()

        self.label = tk.Label(self.master, text="Extract Text dari gambar", font=("Arial", 20, "bold"), fg="white", bg="teal")
        self.label.pack(pady=10)

        self.select_button = tk.Button(self.master, text="Select Image", command=self.select_image, bg="teal")
        self.select_button.pack(pady=10)

        self.extract_button = tk.Button(self.master, text="Extract Text", command=self.extract_text, bg="teal")
        self.extract_button.pack(pady=5)

        self.text_display = tk.Text(self.master, wrap=tk.WORD, width=60, height=15, font=("Arial", 12), bg="white")
        self.text_display.pack(pady=10)

        self.image_label = tk.Label(self.master)
        self.image_label.pack(pady=10)

    def select_image(self):
        image_path = filedialog.askopenfilename(initialdir="/", title="Select An Image", filetypes=(("image files", "*.png;*.jpg;*.jpeg"),))
        if image_path:
            self.image_path.set(image_path)

            image = Image.open(image_path)
            image = image.resize((300, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image=image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo

    def extract_text(self):
        image_path = self.image_path.get()
        if image_path:
            try:
                extracted_text = pytesseract.image_to_string(Image.open(image_path))
                self.text_display.delete(1.0, tk.END)
                self.text_display.insert(tk.END, extracted_text)
            except Exception as e:
                print(f"Error extracting text: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextExtractorApp(root)
    root.mainloop()
