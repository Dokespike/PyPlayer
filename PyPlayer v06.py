#To run the following program, make sure you have Python along with the following Python modules:
#python-imaging-tk
#python-pygame
#Have fun!

import tkFileDialog, PIL.Image, pygame, tkMessageBox
from PIL import ImageTk
from Tkinter import *

confg = []
conf = open('Config.txt')
for x in iter(conf):
	confg.append(x[:-1])
conf.close()

songfolderimp2 = confg[0]
checkforsamesong2 = confg[1]

songfolderimp = songfolderimp2[13:]
checkforsamesong = checkforsamesong2[45:]

print songfolderimp
print checkforsamesong

songfolder = len(songfolderimp) + 1
songlis = []

app = Tk()
app.title('PyPlayer')
ment = StringVar()
pygame.mixer.init()

scrollbar = Scrollbar(app)
scrollbar.grid(row=0, column=0 , sticky = NW)

def initplay(x):
	pygame.mixer.music.load(x)
	pygame.mixer.music.play()
	curts.set('Now Playing: ' + x)
	return

def CurSelet(evt):
    value=(listbox.get(listbox.curselection()))
    initplay(value)

listbox = Listbox(app, selectmode=SINGLE, width='25', height='23')
listbox.bind('<<ListboxSelect>>',CurSelet)
listbox.grid(row=1, column=0 , sticky = NW)

curts = StringVar()
app.geometry('750x500')

f = open('CSI.txt')
for x in iter(f):
	songlis.append(x[songfolder:-1])
	listbox.insert((1), x[songfolder:-1])
f.close()

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

playbut = Button(app, text = 'Pause', command = pygame.mixer.music.pause).place(relx=.495, rely=.5)
pausebut = Button(app, text = 'Play', command = pygame.mixer.music.unpause).place(relx=.5012, rely=.44)

image = PIL.Image.open("Casset logo.png")
photo = ImageTk.PhotoImage(image)
logo = Label(image=photo)
logo.image = photo
logo.grid(row=0, column=0 , sticky = NW)
Curt = Label(app,textvariable = curts).place(relx=.4, rely=.4)

alreadyy = False

def Open():
	myopen = tkFileDialog.askopenfilename()
	if len(myopen) < 4:
		noneadded = tkMessageBox.showwarning( message = 'No song added')
	else:
		addsong(myopen)
		listbox.insert(END, myopen[songfolder:])
		initplay(myopen)

def addsong(x):
	CSI = open('CSI.txt', 'a')
	CSI.write(x+'\n')
	CSI.close()
	
def quit():
	exit = tkMessageBox.askyesno(title="Quit", message = 'Are you sure')
	if exit == True:
		app.destroy()
		sys.exit()
		return

listbox.curselection()

menubar = Menu(app)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'Open', command = Open)
filemenu.add_command(label = 'Export')
filemenu.add_command(label = 'Close',command = quit)
menubar.add_cascade(label = 'File', menu = filemenu)
app.config(menu = menubar)

app.mainloop()
