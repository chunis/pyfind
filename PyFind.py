#! /usr/bin/python

# PyFind  By: Chunchengfh
# About: find file(s) in certain dir(s)

from Tkinter import *

from tkFileDialog import askdirectory
from tkMessageBox import *
from scrolledlist import ScrolledList
import os, sys
import glob
import shutil

Version = '0.1.3'
Author = 'chunchengfh@gmail.com'
Date = '2007.01.08'

class myScrolledList(ScrolledList):
	def runCommand(self, selection):
		for dir in dirnames:
			print dir, 'good'
			tmp_file = os.path.join(dir, selection)
			print 'tmp_file:', tmp_file
			if os.path.exists(tmp_file):
				os.startfile(tmp_file)
				break

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

def mycopy():
	file = scroll.listbox.get('active')
	for dir in dirnames:
		tmp_file = os.path.join(dir, file)
		if os.path.exists(tmp_file):
			tmp_dir = askdirectory()
			print 'copy to: ' + tmp_dir
			shutil.copy(tmp_file, tmp_dir)

def recufind(path, allpath, file):
	if find_flag == False:
		lstatus.config(text='Find is canceled')
		return

	root_width = root.geometry().split('x')[0]
	lstatus.config(width=int(root_width), text='Find files in subdir: ' + allpath + '...')
	os.chdir(path)
	books=glob.glob(file)
	for book in books:
		result.append(allpath + '/' + book)
		scroll.listbox.insert('end', allpath + '/' + book)
#		print path + '/' + book
	for filepath in os.listdir('.'):
		if os.path.isdir(filepath):
			recufind(filepath, allpath+'/'+filepath, file)
	os.chdir('..')

import thread
def myFind():
	global find_flag
	if find_flag == True:
		find_flag = not find_flag
	else:
		thread.start_new(real_find, ())

def real_find():
#	print dirname
	global dirname
	global find_flag

	find_flag = True
	bfind.config(text='Cancel')

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
	recu = var.get()
	file = '*' + keywords + '*.' + type

	root_width = root.geometry().split('x')[0]
#	print 'root_width: '  + root_width
	lstatus.config(width=root_width, text='Find files in dir: ' + dirname + '...')

	global result
	result = [ ]
	books=glob.glob(file)
	for book in books:
		result.append(book)
		scroll.listbox.insert('end', book)
#		print book

	if recu == 1:
		for filepath in os.listdir('.'):
			if os.path.isdir(filepath):
				recufind(filepath, filepath, file)
	
	bfind.config(text='Find')
	if find_flag == True:
		lstatus.config(text='Find finished')
		find_flag = False
	
#	for book in result:
#		scroll.listbox.insert('end', book)

root = Tk()
root.title('PyFind-' + Version)
root.geometry('440x360+250+250')
root.config()
win1 = Frame(root)
win2 = Frame(root)
win3 = Frame(root)
win4 = Frame(root)
win5 = Frame(root)
win6 = Frame(root)	# status bar
#win1.config(width=60)
win1.pack(side=TOP, fill=X)
win2.pack(side=BOTTOM, fill=X)
win6.pack(side=BOTTOM, fill=X)
win3.pack(side=TOP, fill=X)
win4.pack(side=TOP, fill=X)
win5.pack(side=TOP, expand=YES, fill=BOTH)

recu = 0
result = [ ]  # used for store result 
dirname = ''
dirnames = [ ] # used for store old dirs
find_flag = False	# when in find process: true; else: false

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
browse.pack(side=RIGHT, padx=6, pady=6) 
browse.focus()
browse.bind('<Return>', lambda event: brws())

epath = Entry(win3, width=40)
epath.pack(padx=5, side=LEFT, expand=YES, fill=X)
#epath.delete(0, END)
#epath.insert(0, 'E:\New Folder')

Label(win4, text='key word:', font=font3).pack(side=LEFT) #, anchor='e')
ekeyword = Entry(win4, width=20)
ekeyword.pack(padx=5, side=LEFT)
ekeyword.bind('<Return>', lambda event: myFind())

Label(win4, text='type:', font=font3).pack(side=LEFT) #, anchor='e')
etype = Entry(win4, width=6)
#etype.insert(0, 'chm')
etype.insert(0, '*')
etype.pack(padx=5, side=LEFT)
etype.bind('<Return>', lambda event: myFind())

var = IntVar()
#Checkbutton(win4, text='recursive', font=font3, variable=var).pack(padx=5, side=LEFT)
crecu=Checkbutton(win4, text='recursive', font=font3, variable=var)
crecu.pack(padx=5, side=LEFT)
crecu.bind('<Return>', lambda event: myFind())
#var.set(1)

scroll = myScrolledList('', win5)

lstatus = Label(win6, font=font3)
lstatus.config(relief=SUNKEN, padx=2, pady=2)
lstatus.pack(side=LEFT, expand=YES, fill=X)

bquit = Button(win2, text='Quit', command=root.quit)
bquit.config(font=font2, padx=1)

bfind = Button(win2, text='Find', command=myFind)
bfind.config(font=font2, padx=1)
bclear = Button(win2, text='Clean', command=myclear)
bclear.config(font=font2, padx=1)
bopen = Button(win2, text='Open', command=myopen)
bopen.config(font=font2, padx=1)
bopen_dir = Button(win2, text='Open Dir', command=myopen_dir)
bopen_dir.config(font=font2, padx=1)
bcopy = Button(win2, text='Copy to', command=mycopy)
bcopy.config(font=font2, padx=1)

bfind.pack(side=RIGHT, padx=5, pady=3, anchor='s')
bquit.pack(side=LEFT, padx=5, pady=3, anchor='s')
bclear.pack(side=RIGHT, padx=5, pady=3, anchor='s')
bopen.pack(side=RIGHT, padx=5, pady=3, anchor='s')
bopen_dir.pack(side=RIGHT, padx=5, pady=3, anchor='s')
bcopy.pack(side=RIGHT, padx=5, pady=3, anchor='s')

root.mainloop()
