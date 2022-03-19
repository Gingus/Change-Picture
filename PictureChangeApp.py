# Phil Minard
# With help from Miguel Lourenco
import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import sys
import os
from PIL import Image, ImageTk

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "PictureChange.ui")


class PictureChangeApp:
    """This is to show changing a picture placed in a Label"""
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('frame1', master)

        self.labelImage = None
        self.next_picture = None
        self.is_on = None
        builder.import_variables(self, ['labelImage', 'next_picture'])
        builder.import_variables(self, ['is_on'])
        
        builder.connect_callbacks(self)
    
    def button_next_pressed(self):
        """pressing the button to change between the images"""
        puppy_image = 'C:\\location\\of\\Desktop\\your\\first image\\2\\display.jpg'
        Phil_Pic = 'C:\\location\\of\\Desktop\\your\\first image\\2\\display.jpg'
        label = self.builder.get_object('labelPicture')

        if self.is_on:
            on_image = Image.open(Phil_Pic)
            on_image = on_image.resize((450, 350), Image.ANTIALIAS)
            print("Resize of on_image complete")
            image_on = ImageTk.PhotoImage(on_image)
            label.configure(image=image_on)
            label.image = image_on
            self.is_on = False
            print(self.is_on)

        else:
            off_image = Image.open(puppy_image)
            off_image = off_image.resize((450, 350), Image.ANTIALIAS)
            print("Resize of off_image complete")
            image_off = ImageTk.PhotoImage(off_image)
            label.configure(image=image_off)
            label.image = image_off
            self.is_on = True
            print(self.is_on)
        # label.labelImage.update()
        label.pack()

    def run(self):
        """Self explanatory"""
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = PictureChangeApp(root)
    app.run()

