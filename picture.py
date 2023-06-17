from tkinter import *
from PIL import ImageTk, Image

# создание окна

window = Tk()
window.title('картинки')
window.attributes('-fullscreen',True)
window.config(bg='gray')

# настраиваем цвет фона

photoLabel = Label(window,background='black')
photoLabel.pack()

# открываем изображение

current_name_picture = 1
namePicture = f"D:/nikit_OS/picture/pctr/{current_name_picture}.png"
photoPicture = ImageTk.PhotoImage(Image.open(namePicture))
photoLabel.configure(image=photoPicture, width=1000, height=500)
photoLabel.image = photoPicture

# создаём текст в окне

WelcomeLabel = Label(window, text='нажми на любую кнопку',bg='gray')
WelcomeLabel.pack()

# создаём функции, которые открывают картинку и запихивает в label

def nextPhoto():
    global current_name_picture
    current_name_picture = current_name_picture + 1
    if current_name_picture > 3:
        current_name_picture = 1
    namePicture = f'D:/nikit_OS/picture/pctr/{current_name_picture}.png'
    photoPicture = ImageTk.PhotoImage(Image.open(namePicture))
    photoLabel.configure(image=photoPicture,width=1000,height=500)
    photoLabel.image = photoPicture

def backPhoto():
    global current_name_picture
    current_name_picture = current_name_picture - 1
    if current_name_picture < 1:
        current_name_picture = 3
    namePicture = f'D:/nikit_OS/picture/pctr/{current_name_picture}.png'
    photoPicture = ImageTk.PhotoImage(Image.open(namePicture))
    photoLabel.configure(image=photoPicture,width=1000,height=500)
    photoLabel.image = photoPicture

def winDestroy():
    window.destroy()

# привязываем кнопки к картинкам (строка 22,27,32)

btn = Button(text='вперёд>>>',command=nextPhoto,bg='orange',padx=100,pady=50)
btn.pack(side=RIGHT,padx=150,pady=100)
btn1 = Button(text='<<<назад',command=backPhoto,bg='orange',padx=100,pady=50)
btn1.pack(side=LEFT,padx=150,pady=100)
btnDestroy = Button(window,text='выйти',command=winDestroy,bg='orange',padx=50,pady=25)
btnDestroy.pack(padx=20,pady=80)

# цикл окна

window.mainloop()