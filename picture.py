from tkinter import *

window = Tk()
window.title('камни')

StonesLabel = Label(window, background="#000000")
StonesLabel.pack()

def StonesClick():
    StonesPhoto = PhotoImage(file='./rock.png')
    StonesLabel.configure(image=StonesPhoto, width=500, height=500)
    StonesLabel.image = StonesPhoto

WelcomeLabel = Label(window, text='нажми на любую кнопку')
WelcomeLabel.pack()

StonesButton = Button(window, text='камни', command=StonesClick)
StonesButton.pack()

window.mainloop()