#To run the following program, make sure you have Python along with the following Python modules:
#python-imaging-tk
#python-pygame
#Have fun!

import tkFileDialog, PIL.Image, pygame, tkMessageBox
from PIL import ImageTk
from Tkinter import *

CSI = open('directory/CSI.txt', 'a')

app = Tk()
app.title('PyPlayer')
ment = StringVar()
pygame.mixer.init()

scrollbar = Scrollbar(app)
scrollbar.grid(row=0, column=0 , sticky = NW)

listbox = Listbox(app)
listbox.grid(row=0, column=0 , sticky = NW)

songlis = []
song = -1
curts = StringVar()
app.geometry('750x500')

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

playbut = Button(app, text = 'Play', command = pygame.mixer.music.unpause).grid(row=2, column=1)
pausebut = Button(app, text = 'Pause', command = pygame.mixer.music.pause).grid(row=3, column=1)

image = PIL.Image.open("directory/Casset logo.png")
photo = ImageTk.PhotoImage(image)
logo = Label(image=photo)
logo.image = photo
logo.grid(row=0, column=1 , sticky = NW)
Curt = Label(app,textvariable = curts).grid(row=1, column=1)

#entry = Entry(app,textvariable = ment).grid(row=0, column=1)

def Open():
	myopen = tkFileDialog.askopenfilename()
	CSI.write(myopen+'\n')
	listbox.insert((1), myopen)
	curts.set('Now Playing: ' + myopen)
	initplay(myopen)
	return

def initplay(x):
	pygame.mixer.music.load(x)
	pygame.mixer.music.play()
	return

def quit():
	exit = tkMessageBox.askyesno(title="Quit", message = 'Are you sure')
	if exit == True:
		app.destroy()
		sys.exit()
		return

menubar = Menu(app)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'Open', command = Open)
filemenu.add_command(label = 'Export')
filemenu.add_command(label = 'Close',command = quit)

menubar.add_cascade(label = 'File', menu = filemenu)

app.config(menu = menubar)

app.mainloop()
