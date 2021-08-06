from tkinter import *
import tkinter.scrolledtext as st
import requests
mo = Tk()
hel = StringVar()
def func():
	dict6 = {ascii("!source()") : ascii("!init"), "searches for the specified website's source code" : "tries to find if the given text is included in the input"}
	bye = hel.get()
	entry6.delete(0, END)
	if bye == "!help":
		text6.delete("1.0" , END)
		for x, y in dict6.keys() , dict6.values():
			text6.insert(END, x + "\n " + y + "\n")
	else:
		text6.delete("1.0" , END)
		salman = "https://" + bye + ".com"
		r = requests.get(salman)
		text6.insert(END, r.text)
mo.geometry("500x500")
Label5 = Label(mo, text = "Console", fg = "red", font = ("calibre", 30), bg = "black")
Label5.place(relx = 0.17)
text6 = st.ScrolledText(mo, fg = "green", bg = "black", width = 43, height = 20)
text6.place(relx = 0.016, rely = 0.1)
entry6 = Entry(mo, textvariable = hel)
entry6.place(relwidth = 0.6, relheight = 0.05, relx = 0.2, rely = 0.6)
scrollbar = Scrollbar(mo , orient='horizontal', command=text6.xview)
text6['xscrollcommand'] = scrollbar.set
button8 = Button(mo, text = "press", width = 7, height = 2, command = func)
button8.place(relx = 0.36, rely = 0.7)
mo.mainloop()
