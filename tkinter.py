from tkinter import *
import os

mainWindow = Tk()

mainWindow.title('Utility')
mainWindow.geometry('640x550')
mainWindow['padx']=10

label= Label(mainWindow, text='Tkinter geometry')
label.grid(row=0, column=0)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)


fileList = Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for zone in os.listdir('/Windows/System32'):
    fileList.insert(END, zone)

listScroll = Scrollbar(mainWindow, orient=VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand']=listScroll.set

# listScrollX = Scrollbar(mainWindow, orient=HORIZONTAL, command=fileList.xview)
# listScrollX.grid(row=3, column=0, sticky='new', )
# fileList['xscrollcommand'] = listScrollX.set

# Radiobutton Frame

optionFrame = LabelFrame(mainWindow, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

rbvalue = IntVar()
rbvalue.set(1)

radio1 = Radiobutton(optionFrame, text='File Name', value=1, variable=rbvalue)
radio2 = Radiobutton(optionFrame, text='Part', value=2, variable=rbvalue)
radio3 = Radiobutton(optionFrame, text='kman', value=3, variable=rbvalue)

radio1.grid(row=0, column=0, sticky='nw')
radio2.grid(row=1, column=0, sticky='nw')
radio3.grid(row=2, column=0, sticky='nw')

resultLabel = Label(mainWindow, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')

result=Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

timeFrame = LabelFrame(mainWindow, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')

hourspinner = Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minutespinner = Spinbox(timeFrame, width=2, from_=0, to=59)
secondspinner = Spinbox(timeFrame, width=2, from_=0, to=59)

secondspinner.grid(row=0, column=0, sticky='new')
Label(timeFrame, text=":").grid(row=0, column=1, sticky='new')
minutespinner.grid(row=0, column=2, sticky='new')
Label(timeFrame, text=":").grid(row=0, column=3, sticky='new')
hourspinner.grid(row=0, column=4, sticky='new')
timeFrame['padx']=36

dateFrame = Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')

dayLabel=Label(dateFrame, text='Day')
monthLabel=Label(dateFrame, text='Month')
yearLabel=Label(dateFrame, text='Year')

dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

dayspin = Spinbox(dateFrame, width=5, from_=1, to=31)
monthspin = Spinbox(dateFrame, width=5, from_=1, to=12)
yearspin = Spinbox(dateFrame, width=5, from_=2000, to=2099)

dayspin.grid(row=1, column=0, sticky='ew')
monthspin.grid(row=1, column=1, sticky='ew')
yearspin.grid(row=1, column=2, sticky='ew')
dateFrame['padx']=36

okButton = Button(mainWindow, text='OK')
cancelButton = Button(mainWindow, text='Cancel', command=mainWindow.destroy)

okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()

