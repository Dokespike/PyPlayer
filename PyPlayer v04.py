#To run the following program, make sure you have Python along with the following Python modules:
#python-pygame
#The dirrectorys of played music is supposed to be sent to a file called CSI.txt, you can change this as you wish on line 9, but if you dont change it you at least have to make a file titled CSI.txt
#Have fun!

import tkFileDialog, pygame, tkMessageBox
from Tkinter import *

CSI = open('CSI.txt', 'a')

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


Curt = Label(app,textvariable = curts).grid(row=1, column=1)


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
