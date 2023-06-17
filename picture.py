from tkinter import *
from PIL import ImageTk, Image

# создание окна

window = Tk()
window.title('картинки')

# настраиваем цвет фона

photoLabel = Label(window)
photoLabel.pack()

# создаём функции, которые открывают картинку и запихивает в label

current_name_picture = 1
namePicture = f"D:/nikit_OS/picture/pctr/{current_name_picture}.png"
photoPicture = ImageTk.PhotoImage(Image.open(namePicture))
photoLabel.configure(image=photoPicture, width=1000, height=500)
photoLabel.image = photoPicture

# создаём текст в окне

WelcomeLabel = Label(window, text='нажми на любую кнопку')
WelcomeLabel.pack()

def nextPhoto():
    global current_name_picture
    current_name_picture = current_name_picture + 1
    if current_name_picture > 3:
        current_name_picture = current_name_picture - 1
    namePicture = f'D:/nikit_OS/picture/pctr/{current_name_picture}.png'
    photoPicture = ImageTk.PhotoImage(Image.open(namePicture))
    photoLabel.configure(image=photoPicture,width=1000,height=500)
    photoLabel.image = photoPicture

def backPhoto():
    global current_name_picture
    current_name_picture = current_name_picture - 1
    if current_name_picture < 1:
        current_name_picture = current_name_picture + 1
    namePicture = f'D:/nikit_OS/picture/pctr/{current_name_picture}.png'
    photoPicture = ImageTk.PhotoImage(Image.open(namePicture))
    photoLabel.configure(image=photoPicture,width=1000,height=500)
    photoLabel.image = photoPicture


# привязываем кнопки к картинкам (строка 22,27,32)

btn = Button(text='вперёд>>>',command=nextPhoto)
btn.pack()
btn1 = Button(text='<<<назад',command=backPhoto)
btn1.pack()

# цикл окна

window.mainloop()