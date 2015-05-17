#! /usr/bin/python

# PyFind  By: Chunchengfh	at: 2006/11/21
# About: find some file(s) in a certain dir

from Tkinter import *

from tkFileDialog import askdirectory
from tkMessageBox import *
from scrolledlist import ScrolledList
import os, sys
import glob

Version = '0.1.2'
Author = 'chunchengfh@gmail.com'
Date = '2006.12.06'

def myhelp():
	showinfo('Help', '''PyFind can find a certain type of files in a '''
			+ '''certain directory by regular express search. ''')

def myabout():
	showinfo('About', ''' PyFind  --  ''' + Version 
			+ ''' \n\n Python/Tkinter +  py2exe (for .exe file) \n\n Author:\t''' 
			+ Author + '''\n\n Date:\t''' + Date)

def brws():
	global dirname
#	dirname = askdirectory(initialdir = 'c:\\')
	tmp_dir = askdirectory()
#	print dirname
	epath.delete(0, END)
	epath.insert(0, tmp_dir)

def setvar():
	global recu
	recu = var.get()

def myclear():
	scroll.listbox.delete(0, END)

def myopen():
	file = scroll.listbox.get('active')
	print dirnames
	for dir in dirnames:
		print dir, 'good'
		tmp_file = os.path.join(dir, file)
		print 'tmp_file:', tmp_file
		if os.path.exists(tmp_file):
			os.startfile(tmp_file)
			break

def myopen_dir():
	file = scroll.listbox.get('active')
	for dir in dirnames:
		tmp_file = os.path.join(dir, file)
		if os.path.exists(tmp_file):
			print tmp_file
			file_dir = os.path.dirname(tmp_file)
			tmp_dir = os.getcwd()
			os.chdir(file_dir)
			os.startfile('.')
			os.chdir(tmp_dir)

def recufind(path, allpath, file):
	os.chdir(path)
	books=glob.glob(file)
	for book in books:
		result.append(allpath + '/' + book)
#		print path + '/' + book
	for filepath in os.listdir('.'):
		if os.path.isdir(filepath):
			recufind(filepath, allpath+'/'+filepath, file)
	os.chdir('..')

def myFind():
#	print dirname
	global dirname

	dirname = epath.get()
	if not os.path.isdir(dirname):
		showerror('Wrong Path', 'The folder doesn\'t exist. Please correct it first')
		return

	if dirname not in dirnames:
#		dirnames.append(dirname)
		dirnames[:0] = [ dirname ]
	os.chdir(dirname)
	type = etype.get()
	keywords = ekeyword.get()
	file = '*' + keywords + '*.' + type

	global result
	result = [ ]
	books=glob.glob(file)
	for book in books:
		result.append(book)
#		print book

	if recu == 1:
		for filepath in os.listdir('.'):
			if os.path.isdir(filepath):
				recufind(filepath, filepath, file)
	
	for book in result:
		scroll.listbox.insert('end', book)

root = Tk()
root.title('PyFind-' + Version)
#root.config(height=28, width=60)
root.config()
win1 = Frame(root)
win2 = Frame(root)
win3 = Frame(root)
win4 = Frame(root)
win5 = Frame(root)
#win1.config(width=60)
win1.pack(side=TOP, fill=X)
win2.pack(side=BOTTOM, fill=X)
win3.pack(side=TOP, fill=X)
win4.pack(side=TOP, fill=X)
win5.pack(side=TOP, expand=YES, fill=BOTH)

recu = 0
result = [ ]  # used for store result 
dirname = ''
dirnames = [ ] # used for store old dirs

font1 = ('times', 11, 'bold')
font2 = ('times', 13, 'bold')
font3 = ('times', 11, 'normal')

help_button = Button(win1, text='Help', command=myhelp)
help_button.config(bd=2, relief=GROOVE)
help_button.config(font=font1)

about_button = Button(win1, text='About', command=myabout)
about_button.config(bd=2, relief=GROOVE)
about_button.config(font=font1)

labelfont = ('times', 20, 'bold')
lname = Label(win1, text='PyFind', fg='blue')
lname.config(font=labelfont)

help_button.pack(side=LEFT, anchor='n')
about_button.pack(side=RIGHT, anchor='n')
lname.pack(fill=X, pady=20, anchor='s')

Label(win3, text='Find file in:', font=font3).pack(side=LEFT)

browse = Button(win3, text='Browse', command=brws)
browse.config(font=font3, anchor='e')
browse.pack(side=RIGHT, padx=10, pady=10) 
browse.focus()
browse.bind('<Return>', lambda event: brws())

epath = Entry(win3, width=40)
epath.pack(padx=5, side=LEFT)#, fill=X)

Label(win4, text='key word:', font=font3).pack(side=LEFT) #, anchor='e')
ekeyword = Entry(win4, width=20)
ekeyword.pack(padx=5, side=LEFT)

Label(win4, text='type:', font=font3).pack(side=LEFT) #, anchor='e')
etype = Entry(win4, width=6)
etype.insert(0, 'chm')
etype.pack(padx=5, side=LEFT)

var = IntVar()
Checkbutton(win4, text='recursive', font=font3, variable=var, command=setvar).pack(padx=5, side=LEFT)

scroll = ScrolledList('', win5)

bquit = Button(win2, text='Quit', command=root.quit)
bquit.config(font=font2, padx=4)

bfind = Button(win2, text='Find', command=myFind)
bfind.config(font=font2, padx=4)
bclear = Button(win2, text='Clean', command=myclear)
bclear.config(font=font2, padx=4)
bopen = Button(win2, text='Open', command=myopen)
bopen.config(font=font2, padx=4)
bopen_dir = Button(win2, text='Open Dir', command=myopen_dir)
bopen_dir.config(font=font2, padx=4)

bfind.pack(side=RIGHT, padx=5, pady=5, anchor='s')
bquit.pack(side=LEFT, padx=5, pady=5, anchor='s')
bclear.pack(side=RIGHT, padx=5, pady=5, anchor='s')
bopen.pack(side=RIGHT, padx=5, pady=5, anchor='s')
bopen_dir.pack(side=RIGHT, padx=5, pady=5, anchor='s')

root.mainloop()
