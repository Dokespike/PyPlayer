#To run the following program, make sure you have Python along with the following Python modules:
#python-imaging-tk
#python-pygame
#Have fun!

import tkFileDialog, PIL.Image, pygame, tkMessageBox
from PIL import ImageTk
from Tkinter import *


#Opens the config file and puts it into list 'confg'
#The [:-1] from the string removes the break symbol
confg = []
conf = open('Config.txt')
for configuration in iter(conf):
	confg.append(configuration[:-1])
conf.close()


#Grabbing items from array
songfolderimp = confg[0][13:]
checkforsamesong = confg[1][45:]


#Songfolder length is used mainly to chop off dirrectorys for music
songfolder = len(songfolderimp) + 1


#Creates TKinter window and its loop (As well as pygame)
app = Tk()
app.title('PyPlayer')
pygame.mixer.init()


#Scrolling????
scrollbar = Scrollbar(app)
scrollbar.grid(row=0, column=0 , sticky = NW)


#  FFFFFFF                         T                      SSSS   !  
#  F                       CCCC    T    i   OOOO         S       !  
#  FFFF   U   U    NNNN   C      TTTTT     O    O  NNNN   SSSS   !  
#  F      U   Uu   N   N  C        T    I  O    O  N   N      S    
#  F      UUUUU u  N   N   CCCC    T    I   OOOO   N   N  SSSS   !  
#PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP

def initplay(song):
	pygame.mixer.music.load(song)
	pygame.mixer.music.play()
	curts.set('Now Playing: ' + song)
	return


def CurSelet(evt):
    value=(listbox.get(listbox.curselection()))
    initplay(value)

    
def Open():
	myopen = tkFileDialog.askopenfilename()
	if len(myopen) < 4:
		noneadded = tkMessageBox.showwarning( message = 'No song added')
		curts.set('              No song added')
	else:
		addsong(myopen)
		listbox.insert(END, myopen[songfolder:])
		initplay(myopen[songfolder:])
		curts.set('Now Playing: ' + myopen[songfolder:])


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


#Creats listbox, 2nd line allows for selection of items within
listbox = Listbox(app, selectmode=SINGLE, width='25', height='25')
listbox.bind('<<ListboxSelect>>',CurSelet)
listbox.grid(row=1, column=0 , sticky = NW)


#curts is the text variable above play button
curts = StringVar()
app.geometry('750x500')


#Add music to listbox from CSI
songdir = open('CSI.txt')
for song in iter(songdir):
	listbox.insert((1), song[songfolder:-1])
songdir.close()


#Scrolling stuff for listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


#Pause and Play button
playbut = Button(app, text = 'Pause', command = pygame.mixer.music.pause).place(relx=.495, rely=.5)
pausebut = Button(app, text = 'Play', command = pygame.mixer.music.unpause).place(relx=.5012, rely=.44)


#The PyPlayer logo
image = PIL.Image.open("Casset logo.png")
photo = ImageTk.PhotoImage(image)
logo = Label(image=photo)
logo.image = photo
logo.grid(row=0, column=0 , sticky = NW)


#used to put text above pause button, mostly song info
Text = Label(app,textvariable = curts).place(relx=.4, rely=.4)


#Jazz hands
menubar = Menu(app)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'Open', command = Open)
filemenu.add_command(label = 'Export')
filemenu.add_command(label = 'Close',command = quit)
menubar.add_cascade(label = 'File', menu = filemenu)
app.config(menu = menubar)

app.mainloop()
