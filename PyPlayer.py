#To run the following program, make sure you have Python along with the following Python modules:
#python-imaging-tk
#python-pygame
#Have fun!

import tkFileDialog, PIL.Image, pygame, tkMessageBox
from PIL import ImageTk
from Tkinter import *



#This is what makes PyPlayer work, playing the files, organizing it in the program window, and saving it in a dirrectorys file. It does EVERYTHING KNOWN TO MAN. (kind of)

class pyplayer:

	def initplay(self,song):
		print(song)
		pygame.mixer.music.load(song)
		pygame.mixer.music.play()
		curts.set('Now Playing: ' + song[len(songfolder):])
		print('Now Playing: ' + song[len(songfolder):])
		print curts.get
		return
	
	
	    
	def Open(self):
		myopen = tkFileDialog.askopenfilename()
		if len(myopen) < 4:
			noneadded = tkMessageBox.showwarning( message = 'No song 	added')
			curts.set('              No song added')
		if CheckForSameSong == '1':
			numberofsongs = len(musiclist)
			samesong = False
			x = 0
			for song in musiclist:
				x += 1
				if song == myopen:
					samesong = True
				if x == numberofsongs:
					if samesong == True:
						alreadyhere = 	tkMessageBox.showwarning( message = 'Song already added')
					else:
						Pp.addsong(myopen)
						listbox.insert(END, myopen[len	(songfolder):])
						Pp.initplay(myopen)
		
		else:
			Pp.addsong(myopen)
			listbox.insert(END, myopen[len(songfolder):])
			Pp.initplay(myopen)

	def delete(self):
		print get(ACTIVE)
		listbox.delete(ANCHOR)
		CSI = open('MusicDir.txt', 'w')
		for song in listbox:
			CSI.write(song+'\n')
			CSI.close()


	def addsong(self,x):
		CSI = open('MusicDir.txt', 'a')
		CSI.write(x+'\n')
		CSI.close()
	
	def SetVolume(self):
		volumeSlider = volume.get() + .0
		newVolume = volumeSlider/100
		pygame.mixer.music.set_volume(newVolume)

	
	def quit():
		exit = tkMessageBox.askyesno(title="Quit", message = 'Are you sure')
		if exit == True:
			app.destroy()
			sys.exit()
			return







#Creates TKinter and starts its loop, makes Pp to use the above class (pyplayer), starts pygames mixer (used to play sounds), and makes a list used to store info about the songs in the program.
musiclist = []
Pp = pyplayer()
app = Tk()
app.title('PyPlayer')
app.geometry('750x500')
pygame.mixer.init()



#Makes the listbox and places it in the window
listbox = Listbox(app, selectmode=SINGLE, width='93', height='27')
listbox.grid(row=1, column=0 )



#Opens the config file and puts each line into the list 'confg'
#The [:-1] removes the break symbol from the end of each line (/n)
confg = []
conf = open('Config.txt')
for configuration in iter(conf):
	confg.append(configuration[:-1])
conf.close()



#Grabbing relevent info from the confg list to use in program
#The chopping in these strings removes non-needed text
songfolder = confg[0][13:]
CheckForSameSong = confg[1][25:]
VolumeControl = confg[2][21:]
Logo = confg[3][21:]
ArrowBrowser = confg[4][35:]



#This prints out info about the config to console.
print('\nPyPlayer is Licensed under the MIT license (Do what ever you want nerd!)\n\nLoaded config is as follows:\n===============================\nsongfolder: ' + songfolder +'\nCheckForSameSong: ' +  CheckForSameSong + '\nVolumeControl: ' + VolumeControl + '\nLogo: ' + Logo + '\nArrowBrowser: ' + ArrowBrowser + '\n===============================\n')



#Add items to listbox from the file MusicDir
#The [:-1] removes the break symbol from the end of each line (/n)
songdir = open('MusicDir.txt')
for song in iter(songdir):
	listbox.insert((1), song[len(songfolder):-1])
	musiclist.append(song[:-1])
songdir.close()



#On select in listbox, take songfolderimp plus song name(value) and play it
def CurSelect(evt):
    value=(listbox.get(listbox.curselection()))
    Pp.initplay(songfolder + value)
listbox.bind('<<ListboxSelect>>',CurSelect)
		


#The PyPlayer logo
if Logo == '1':
	image = PIL.Image.open("logo.png")
	photo = ImageTk.PhotoImage(image)
	logo = Label(image=photo)	
	logo.image = photo
	logo.grid(row=0, column=0 , sticky = NW)


#Arrows for moving up and down listbox
if ArrowBrowser == '1':
	scrollbar = Scrollbar(app)
	scrollbar.place(relx=.435, rely=.03)
	listbox.config(yscrollcommand=scrollbar.set)
	scrollbar.config(command=listbox.yview)



#Slider and button to change volume of music
if VolumeControl == '1':
	volume = Scale(app, from_=0, to=100, length=200, orient=HORIZONTAL)
	volume.place(relx=.62, rely=.01)
	VolumeButton = Button(app, text= 'Volume', command = Pp.SetVolume).place(relx=.9, rely=.03)



#Pause and Play button
playbut = Button(app, text = 'Play', command = pygame.mixer.music.unpause).place(relx=.458, rely=.03)
pausebut = Button(app, text = 'Pause', command = pygame.mixer.music.pause).place(relx=.53, rely=.03)



#curts is the text variable on the window
curts = StringVar()
Text = Label(app,textvariable = curts)
if Logo == '1':
	Text.place(relx=.215, rely=.135)
else:
	Text.place(relx=.45, rely=.1)



#Jazz hands
menubar = Menu(app)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'Import', command = Pp.Open)
filemenu.add_command(label = 'Delete', command = Pp.delete)
filemenu.add_command(label = 'Close',command = Pp.quit)
menubar.add_cascade(label = 'File', menu = filemenu)
app.config(menu = menubar)



app.mainloop()
