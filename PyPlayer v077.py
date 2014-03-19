#To run the following program, make sure you have Python along with the following Python modules:
#python-imaging-tk
#python-pygame
#Have fun!

import tkFileDialog, PIL.Image, pygame, tkMessageBox
from PIL import ImageTk
from Tkinter import *



#Creates TKinter window and its loop (As well as pygames loop (mixer))
musiclist = []
app = Tk()
app.title('PyPlayer')
app.geometry('750x500')
pygame.mixer.init()



#Makes the listbox and places it
listbox = Listbox(app, selectmode=SINGLE, width='93', height='27')
listbox.grid(row=1, column=0 )



#Opens the config file and puts it into list 'confg'
#The [:-1] removes the break symbol from each segment (/n)
confg = []
conf = open('Config.txt')
for configuration in iter(conf):
	confg.append(configuration[:-1])
conf.close()



#Grabbing items from confg to use in program
songfolderimp = confg[0][13:]
CheckForSameSong = confg[1][25:].upper()
VolumeControl = confg[2][21:].upper()

#Songfolder length is used mainly to chop strings for music
songfolder = len(songfolderimp) + 1



#Add music to listbox from MusicDir
#The [:-1] removes the break symbol from each segment (/n)
songdir = open('MusicDir.txt')
for song in iter(songdir):
	listbox.insert((1), song[songfolder:-1])
	musiclist.append(song[:-1])
songdir.close()


def CurSelet(evt):
    value=(listbox.get(listbox.curselection()))
    initplay(value)
listbox.bind('<<ListboxSelect>>',CurSelet)



def initplay(song):
	pygame.mixer.music.load(song)
	pygame.mixer.music.play()
	curts.set('Now Playing: ' + song)
	return


    
def Open():
	myopen = tkFileDialog.askopenfilename()
	if len(myopen) < 4:
		noneadded = tkMessageBox.showwarning( message = 'No song added')
		curts.set('              No song added')
	if CheckForSameSong == 'Y':
		numberofsongs = len(musiclist)
		print numberofsongs
		samesong = False
		x = 0
		for song in musiclist:
			x += 1
			if song == myopen:
				samesong = True
			if x == numberofsongs:
				if samesong == True:
					alreadyhere = tkMessageBox.showwarning( message = 'Song already added')
				else:
					addsong(myopen)
					listbox.insert(END, myopen[songfolder:])
					initplay(myopen[songfolder:])
	
	else:
		addsong(myopen)
		listbox.insert(END, myopen[songfolder:])
		initplay(myopen[songfolder:])

def delete():
	print get(ACTIVE)
	listbox.delete(ANCHOR)


def addsong(x):
	CSI = open('CSI.txt', 'a')
	CSI.write(x+'\n')
	CSI.close()
	
def SetVolume():
	volumeSlider = volume.get() + .0
	newVolume = volumeSlider/100
	pygame.mixer.music.set_volume(newVolume)

	
def quit():
	exit = tkMessageBox.askyesno(title="Quit", message = 'Are you sure')
	if exit == True:
		app.destroy()
		sys.exit()
		return
		


#The PyPlayer logo
image = PIL.Image.open("logo.png")
photo = ImageTk.PhotoImage(image)
logo = Label(image=photo)
logo.image = photo
logo.grid(row=0, column=0 , sticky = NW)


#Arrows for moving up and down listbox
scrollbar = Scrollbar(app)
scrollbar.place(relx=.435, rely=.03)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)



#Slider and button to change volume of music
if VolumeControl == 'Y':
	volume = Scale(app, from_=0, to=100, length=200, orient=HORIZONTAL)
	volume.place(relx=.62, rely=.01)
	VolumeButton = Button(app, text= 'Volume', command = SetVolume).place(relx=.9, rely=.03)



#Pause and Play button
playbut = Button(app, text = 'Play', command = pygame.mixer.music.unpause).place(relx=.458, rely=.03)
pausebut = Button(app, text = 'Pause', command = pygame.mixer.music.pause).place(relx=.53, rely=.03)



#curts is the text variable on the window
curts = StringVar()
Text = Label(app,textvariable = curts).place(relx=.215, rely=.135)



#Jazz hands
menubar = Menu(app)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'Import', command = Open)
filemenu.add_command(label = 'Delete', command = delete)
filemenu.add_command(label = 'Close',command = quit)
menubar.add_cascade(label = 'File', menu = filemenu)
app.config(menu = menubar)



app.mainloop()