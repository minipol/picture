from tkinter import *
from PIL import ImageTk, Image

# создание окна

window = Tk()
window.title('картинки')
window.attributes('-fullscreen',True)

# настраиваем цвет фона

StonesLabel = Label(window)
StonesLabel.pack()
KolbosaLabel = Label(window)
KolbosaLabel.pack()
SaulLabel = Label(window)
SaulLabel.pack()

# создаём картинки

def StonesClick():
    StonesPhoto = PhotoImage(file="D:/nikit_OS/picture/rock.png")
    StonesLabel.configure(image=StonesPhoto, width=1000, height=500)
    StonesLabel.image = StonesPhoto

def KolbosaClick():
    KolbosaPhoto = ImageTk.PhotoImage(Image.open('D:/nikit_OS/picture/kolbosa.png'))
    StonesLabel.configure(image=KolbosaPhoto,width=1000,height=500)
    StonesLabel.image = KolbosaPhoto

def SaulClick():
    SaulPhoto = ImageTk.PhotoImage(Image.open('D:/nikit_OS/picture/saul goodman.png'))
    StonesLabel.configure(image=SaulPhoto,width=1000,height=500)
    StonesLabel.image = SaulPhoto

# создаём текст в окне

WelcomeLabel = Label(window, text='нажми на любую кнопку')
WelcomeLabel.pack()

# привязываем кнопки к картинкам (строка 22,27,32)

StonesButton = Button(window, text='камни', command=StonesClick)
StonesButton.pack()
KolbosaButton = Button(window,text='деловая колбоса',command=KolbosaClick)
KolbosaButton.pack()
SaulButton = Button(window,text='человек',command=SaulClick)
SaulButton.pack()

# цикл окна

window.mainloop()