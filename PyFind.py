#! /usr/bin/python

# PyFind (0.1) By: Chunchengfh	at: 2006/11/21
# About: find some file(s) in a certain dir

from Tkinter import *

from tkFileDialog import askdirectory
from tkMessageBox import showinfo
from scrolledlist import ScrolledList
import os, sys
import glob

Version = str(0.1)
Author = 'Chunchengfh@gmail.com'
Date = '2006.11.21'

def myhelp():
	showinfo('Help', '''PyFind can find a certain type of files in a '''
			+ '''certain directory by regular express search. ''')

def myabout():
	showinfo('About', ''' PyFind  --  ''' + Version 
			+ ''' \n\n Python/Tkinter +  py2exe (for .exe file) \n\n''' 
			+ Author + '''\n\n ''' + Date)

def brws():
	global dirname
#	dirname=askdirectory(initialdir = 'c:\\')
	dirname=askdirectory()
#	print dirname
	epath.delete(0, END)
	epath.insert(0, dirname)

def setvar():
	global recu
	recu = var.get()

def myclear():
	scroll.listbox.delete(0, END)

def myopen():
	file = scroll.listbox.get('active')
	os.startfile(file)

def myopen_dir():
	file = scroll.listbox.get('active')
	file_dir = os.path.dirname(file)
#	print file_dir
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
	os.chdir(dirname)
	type = etype.get()
	keywords = ekeyword.get()
	file = '*' + keywords + '*.' + type

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
root.config(height=28, width=60)
win1 = Frame(root)
win2 = Frame(root)
win3 = Frame(root)
win4 = Frame(root)
#win1.config(width=60)
win1.pack(side=TOP, fill=X)
win2.pack(side=BOTTOM, fill=X)
win4.pack(side=BOTTOM, fill=X)
win3.pack(side=BOTTOM, fill=X)

recu = 0
result = [ ]  # used for store result 

font_1 = ('times', 11, 'bold')
font_2 = ('times', 13, 'bold')
font_3 = ('times', 11, 'normal')

help_button = Button(win1, text='Help', command=myhelp)
help_button.config(bd=2, relief=GROOVE)
help_button.config(font=font_1)

about_button = Button(win1, text='About', command=myabout)
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
browse.focus()
browse.bind('<Return>', lambda event: brws())

epath = Entry(root, width=40)
epath.pack(padx=5, side=LEFT)

Label(win3, text='key word', font=font_3).pack(side=LEFT, anchor='e')
ekeyword = Entry(win3, width=20)
ekeyword.pack(padx=5, side=LEFT)

Label(win3, text='type', font=font_3).pack(side=LEFT, anchor='e')
etype = Entry(win3, width=6)
etype.insert(0, 'chm')
etype.pack(padx=5, side=LEFT)

var = IntVar()
Checkbutton(win3, text='recursive', font=font_3, variable=var, command=setvar).pack(side=LEFT)

scroll = ScrolledList('', win4)

bquit = Button(win2, text='Quit', command=root.quit)
bquit.config(font=font_1, padx=6)

bsort = Button(win2, text='Find', command=myFind)
bsort.config(font=font_2, padx=6)
bclear = Button(win2, text='Clear', command=myclear)
bclear.config(font=font_2, padx=6)
bopen = Button(win2, text='Open', command=myopen)
bopen.config(font=font_2, padx=6)
bopen_dir = Button(win2, text='Open Dir', command=myopen_dir)
bopen_dir.config(font=font_2, padx=6)

bquit.pack(side=LEFT, padx=5, pady=5, anchor='se')
bclear.pack(side=LEFT, padx=5, pady=5, anchor='s')
bopen.pack(side=LEFT, padx=5, pady=5, anchor='s')
bopen_dir.pack(side=LEFT, padx=5, pady=5, anchor='s')
bsort.pack(side=RIGHT, padx=5, pady=5, anchor='s')

root.mainloop()
