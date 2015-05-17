#! /usr/bin/python

# PyFind (0.0.1) By: denny.deng  at: 2006/11/10
# About: find some file(s) in a certain dir

from Tkinter import *
from tkFileDialog import askdirectory

import os, sys
import glob


root = Tk()
root.title('PyFind-0.0.1')
root.config(height=28, width=40)
win1 = Frame(root)
win2 = Frame(root)
win3 = Frame(root)
#win1.config(width=60)
win1.pack(side=TOP, fill=X)
win2.pack(side=BOTTOM, fill=X)
win3.pack(side=BOTTOM, fill=X)

def brws():
	global dirname
	dirname=askdirectory()
	print dirname
#	epath.config(text=filename)
	epath.insert(0,dirname)

def setvar():
	global recu
	recu = var.get()

def recufind(path, file):
	os.chdir(path)
	books=glob.glob(file)
	for book in books:
		print path + '/' + book
	for filepath in os.listdir('.'):
		if os.path.isdir(filepath):
			recufind(filepath, file)
	os.chdir('..')

def myFind():
	print dirname
	os.chdir(dirname)
	type = etype.get()
	keywords = ekeyword.get()
	file = '*' + keywords + '*.' + type

	books=glob.glob(file)
	for book in books:
		print book

	if recu == 1:
		for filepath in os.listdir('.'):
			if os.path.isdir(filepath):
				recufind(filepath, file)


font_2 = ('times', 13, 'bold')
font_3 = ('times', 11, 'normal')

from tkMessageBox import showinfo
font_1 = ('times', 11, 'bold')

def myhelp():
	showinfo('Help', '''PyFind can find a certain type of files in a certain directory by regular express search. ''')

def myabout():
	showinfo('About', ''' PyFind -- 0.0.1 \n\n Python/Tkinter +  py2exe (for .exe file) \n\n Denny Deng / 2006.11.10
		''')

def myabout2(x):
	str = x[0] + ' -- ' + x[1] + '\0\0 Python/Tkinter + py2exe (for .exe file) \n\n'
	str += 'Date: ' + x[2]
	#showinfo('About', ''' PyFind -- 0.0.1 \n\n Python/Tkinter +  py2exe (for .exe file) \n\n Date: 2006.09.17
		#''')
	showinfo('About', str)

help_button = Button(win1, text='Help', command=myhelp)
help_button.config(bd=2, relief=GROOVE)
help_button.config(font=font_1)

about_button = Button(win1, text='About', command=myabout)
#about_button = Button(win1, text='About', command=lambda x: myabout2((PyFind, 0.0.1, 2006.09.17))
about_button.config(bd=2, relief=GROOVE)
about_button.config(font=font_1)

labelfont = ('times', 20, 'bold')
lname = Label(win1, text='PyFind', fg='blue')
lname.config(font=labelfont)

help_button.pack(side=LEFT, anchor='n')
lname.pack(side=LEFT, expand=YES, fill=X, pady=30, anchor='s')
about_button.pack(side=RIGHT, anchor='n')

Label(root, text='Find file in:', font=font_3).pack(side=TOP, anchor='w')

browse = Button(root, text='Browse', command=brws)
browse.config(font=font_3)
browse.pack(side=RIGHT, padx=20, pady=25) 
epath = Entry(root, width=40)
epath.pack(padx=5, side=LEFT)

Label(win3, text='key word', font=font_3).pack(side=LEFT, anchor='e')
ekeyword = Entry(win3, width=20)
ekeyword.pack(padx=5, side=LEFT)

Label(win3, text='type', font=font_3).pack(side=LEFT, anchor='e')
etype = Entry(win3, width=8)
etype.pack(padx=5, side=LEFT)

var = IntVar()
Checkbutton(win3, text='recursive', variable=var, command=setvar).pack(side=LEFT)

bquit = Button(win2, text='Quit', command=root.quit)
bquit.config(font=font_1, padx=6)

bsort = Button(win2, text='Find', command=myFind)
bsort.config(font=font_2, padx=6)

bquit.pack(side=RIGHT, padx=5, pady=5, anchor='se')
bsort.pack(side=BOTTOM, padx=5, pady=5, anchor='s')

root.mainloop()
