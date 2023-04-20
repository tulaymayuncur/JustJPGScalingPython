
#Tülay MAYUNCUR - 2004040016


from contextlib import nullcontext
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image
from tkinter import Entry
import cv2



class ImageResize:
    def __init__(self, path=""):
         self._path = path

    # getter method
    def get_Path(self):
        return self._path

    # setter method
    def set_Path(self, x):
        self._path = x



my_w = tk.Tk()
my_w.geometry("800x800")  # Size of the window
my_w.title('Image Picker')
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(my_w, text='Add Photo', width=30, font=my_font1)
l1.grid(row=1, column=1)
b1 = tk.Button(my_w, text='Upload File',
               width=20, command=lambda: upload_file())
b1.grid(row=2, column=1)




def upload_file():

    global img, wNew, hNew #newSize

    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    print(filename)
    filePath = filename
    img = ImageTk.PhotoImage(file=filePath)
    b2 = tk.Button(my_w, image=img)  # using Button
    b2.grid(row=3, column=1)

    imgOpenCv = cv2.imread(filename=filePath)  # Resmin orijinal hali
    print(imgOpenCv.shape)  # (wight,height,kanal)
    resImg = ImageResize()
    resImg.set_Path(filePath )
# Widhts

    my_font2 = ('times', 14)
    lw = tk.Label(my_w, text='Widht Size :', width=30, font=my_font2)
    # lw.grid(row=4,column=1)
    lw.place(x=-3, y=560)

    wEntry = tk.Entry(my_w, width=10)
    # self.wEntry.grid(row=5,column=1)
    wEntry.place(x=75, y=580)

    #bw = tk.Button(my_w,text='Enter')
    # bw.grid(row=6,column=1)
    # bw.place(x=75,y=610)

# Height

   # lh = tk.Label(my_w, text='Height Size :', width=30, font=my_font2)
    # lh.grid(row=4,column=2)
    #lh.place(x=175, y=560)

    #hEntry = tk.Entry(my_w, width=10)
    # hEntry.grid(row=5,column=2)
    #hEntry.place(x=250, y=580)

    buttonEnter = tk.Button(my_w, text='Enter', command=lambda: boyutlandirma(filePath, wEntry=wEntry))
    # bh.grid(row=6,column=2)
    buttonEnter.place(x=425, y=580)

    

    # dim = (width, height)
    # imageresized = cv2.resize(imgOpenCv, dim)
    # cv2.imshow("resize",imageresized)
    # file_save(imageresized)

    cv2.destroyAllWindows()



def boyutlandirma(filePath,self=None,wEntry=Entry):

    resImg = ImageResize()
    newPath = resImg.get_Path()
    print("----------" + newPath)
    wNew = int(wEntry.get())
   # hNew = int(hEntry.get())

    

    #print(newSize)

    imgOpenCv = cv2.imread(filename=filePath)  # Resmin orijinal hali
    print(imgOpenCv.shape)  # (wight,height,kanal)

    hNew =int((imgOpenCv.shape[0]/imgOpenCv.shape[1])*wNew)
    # wNew*imgOpenCv.shape[1]/100 + imgOpenCv.shape[1]


    resize = cv2.resize(imgOpenCv, (wNew, hNew))
    cv2.imshow("Resized", resize)
    print(wNew,hNew)

    #file_save(resize)

    saveButton = tk.Button(my_w, text="Save",command=lambda:file_save(resize))
    #saveButton.grid(row=7,column=2)
    saveButton.place(x=500,y=580)


def file_save(resize):
    f = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    cv2.imwrite(f.name,resize)
   
    f.close() # `()` was missing.





# def button_command():
    #  return None
   #   print("deneme")



my_w.mainloop()
