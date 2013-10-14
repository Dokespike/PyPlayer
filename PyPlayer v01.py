#sudo apt-get install python-imaging-tk, and pygame
import tkFileDialog, PIL.Image, pygame, tkMessageBox
from PIL import ImageTk
from Tkinter import *

app = Tk()
app.title('PyPlayer')
ment = StringVar()
pygame.mixer.init()


songnum = -1
songlis = []



app.geometry('750x500+500+300')



playbut = Button(app, text = 'Play', command = pygame.mixer.music.unpause).grid(row=1, column=0)
pausebut = Button(app, text = 'Pause', command = pygame.mixer.music.pause).grid(row=2, column=0)




image = PIL.Image.open("Casset.png")
photo = ImageTk.PhotoImage(image)
logo = Label(image=photo)
logo.image = photo

logo.grid(row=0, column=0 , sticky = NW)






#entry = Entry(app,textvariable = ment).grid(row=0, column=1)





def Open():
	myopen = tkFileDialog.askopenfilename()
	label32 = Label(app, text = myopen, command = initplay(myopen)).pack()
	return


def initplay(x):
	pygame.mixer.music.load(x)
	pygame.mixer.music.play()
	return


def quit():
	exit = tkMessageBox.askyesno(title="Quit", message = 'Are you sure')
	if exit == True:
		app.destroy()
		return







menubar = Menu(app)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'Import', command = Open)
filemenu.add_command(label = 'Export')
filemenu.add_command(label = 'Close',command = quit)

menubar.add_cascade(label = 'File', menu = filemenu)


app.config(menu = menubar)









app.mainloop()
