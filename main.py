from tkinter import Tk, filedialog, messagebox, ttk
from PIL import Image, ImageTk
import image_classification

# Image Browser
def browseFile():
    path = filedialog.askopenfilename(
        initialdir="/", title="Select an Image", filetypes=(("Image", "*.jpg*"), ("All files", "*.*")))

    showText(image_classification.classify(path))
    showImage(path)


master = Tk()

# Window Management
master.title('Image Classification AI')
master.state('zoomed')
master.resizable(True, True)

# Frame Management
header_frame = ttk.Frame(master)
header_frame.pack()

body_frame = ttk.Frame(master)
body_frame.pack()

smart_list = ttk.Frame(body_frame)
smart_list.grid(column=0, columnspan=2, row=0, pady=20)

# Widgets Management
header = ttk.Label(
    header_frame, text="Image Classification AI")
header.grid(row=0, column=0, pady=3)
header.config(background='#09509e', foreground="#e7e6e6",
              width=1920, font=('Constantia', 24, 'bold'))

caption = ttk.Label(body_frame, text="", font="Calibri 25 bold")
caption.grid(row=1, column=0, columnspan=3, pady=10)

confidence = ttk.Label(body_frame, text="", font="Calibri 25 bold")
confidence.grid(row=2, column=0, columnspan=3, pady=10)


camera_button=ttk.Button(body_frame, text = 'Open Image', width = 25, command = browseFile)
camera_button.grid(row = 3, column = 0, pady = 10)

label=ttk.Label(body_frame, text="", image="")
label.grid(row = 5)


def showText(Classification):
    text1 = 'This is {} ' .format(Classification[0])
    caption.config(text = text1)

    text2 = 'I am {:.0f}% sure.' .format(Classification[1])
    confidence.config(text = text2)

    
def showImage(image_path):
    image=Image.open(image_path)
    photo=ImageTk.PhotoImage(image)

    label.config(image = photo)
    label.image=photo
    
master.mainloop()
