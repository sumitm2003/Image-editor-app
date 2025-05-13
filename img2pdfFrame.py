from tkinter import Button, LEFT, Toplevel
from tkinter import filedialog
import cv2


class Img2pdfFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.img2pdf_button = Button(self, text="IMG2PDF")
        self.cancel_button = Button(self, text="Cancel")

        self.img2pdf_button.bind("<ButtonRelease>", self.img2pdf_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.img2pdf_button.pack(side=LEFT)
        self.cancel_button.pack()

    def img2pdf_button_released(self, event):

        original_file_type = self.master.filename.split('.')[-1]
        filename = filedialog.asksaveasfilename()
        filename = filename + "." + original_file_type

        save_image = self.master.processed_image
        cv2.imwrite(filename, save_image)

        self.master.filename = filename








    def cancel_button_released(self, event):

        self.master.image_viewer.show_image()
        self.close()

    def close(self):
        self.destroy()