import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Label, font
from PIL import Image, ImageTk
import pillow_avif                  #only for avif file format

def import_file():
    global img,file_path
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg; *.webp, *.avif")]
    file_path = tk.filedialog.askopenfilename(title="Select a file", filetypes=fileTypes)
    print(file_path)
    label.config(text=f"Image loaded:{file_path}")
    if file_path:
        img = Image.open(file_path)


def convert():
    global img
    outf = combobox.get()
    print(outf)
    if file_path[-3:] == outf:
        print("the fileformats are the same, choce another one") #hacer con un mgsbox
    else:
        export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("Image files", f"{outf}")])
        img.save(export_file_path)
        messagebox.showinfo(title="Completed Conversion" ,message="Succesfully Converted!")


root = tk.Tk()
root.title("Image File Converter")
root.geometry("600x220")
import_b = tk.Button(root, text="Import File", font="Arial 14",command=import_file)
import_b.pack(pady=20)
label = Label(text="")
label.pack(pady=10)
combobox = ttk.Combobox(root, values=[".jpg", ".png", ".tga", ".bmp", ".webp"])
combobox.pack()
convert_b = tk.Button(root, text="Convert", font="Arial 14",command=convert)
convert_b.pack(pady=20)
root.mainloop()