#To run the following program, make sure you have Python along with the following Python modules:
#python-imaging-tk
#python-pygame
#Have fun!

import tkFileDialog, PIL.Image, pygame, tkMessageBox
from PIL import ImageTk
from os import listdir

musiclist = []

#Opens the config file and puts it into list 'confg'
#The [:-1] from the string removes the break symbol
confg = []
conf = open('Config.txt')
for configuration in iter(conf):
	confg.append(configuration[:-1])
conf.close()


#Grabbing items from array
songfolderimp = confg[0][13:]
CheckForSameSong = confg[1][25:].upper()
VolumeControl = confg[2][21:].upper()



#Songfolder length is used mainly to chop off dirrectorys for music
songfolder = len(songfolderimp) + 1


#Creates TKinter window and its loop (As well as pygame)
songplaying = ''
app = Tk()
app.title('PyPlayer')
pygame.mixer.init()


#curts will be what ever song is playing (what is put into initplay)
curts = StringVar()


#Scrolling????
scrollbar = Scrollbar(app)
scrollbar.grid(row=0, column=0 , sticky = NW)




def CurSelet(evt):
    value=(listbox.get(listbox.curselection()))
    initplay(value)



#Creats listbox, 2nd line allows for selection of items
listbox = Listbox(app, selectmode=SINGLE, width='25', height='25')
listbox.bind('<<ListboxSelect>>',CurSelet)
listbox.grid(row=1, column=0 , sticky = NW)



#Add music to listbox from CSI
#The [:-1] from the string removes the break symbol
songdir = open('CSI.txt')
for song in iter(songdir):
	listbox.insert((1), song[songfolder:-1])
	musiclist.append(song[:-1])
songdir.close()

print musiclist


def initplay(song):
	pygame.mixer.music.load(song)
	pygame.mixer.music.play()
	curts.set('Now Playing: ' + song)
	return

#tkMessageBox.showwarning( message = 'Song already added')
    
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
		


#Slider to change volume of music
if VolumeControl == 'Y':
	volume = Scale(app, from_=100, to=0, length=200)
	volume.place(relx=.9, rely=.518)
	VolumeButton = Button(app, text= 'Volume', command = SetVolume).place(relx=.822, rely=.87)




#curts is the text variable above play button
curts = StringVar()
app.geometry('750x500')


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


#used to place curts in the program
Text = Label(app,textvariable = curts).place(relx=.28, rely=.16)	


#Jazz hands
menubar = Menu(app)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'Import', command = Open)
filemenu.add_command(label = 'Delete', command = delete)
filemenu.add_command(label = 'Close',command = quit)
menubar.add_cascade(label = 'File', menu = filemenu)
app.config(menu = menubar)

app.mainloop()
