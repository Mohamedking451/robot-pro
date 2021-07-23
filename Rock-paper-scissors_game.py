from tkinter import *
from time import sleep
import random
from tkinter.colorchooser import askcolor
mo = Tk()
salah = StringVar()
hello = Text(mo, width = 36, height = 20)
hello.place(relx = 0.5 , rely = 0.3, anchor = "center")
def rock(thing):
	x = thing
	def time():
			list6 = ["rock", "paper", "scissors"]
			bot = random.choice(list6)
			hello.insert(END, bot)
			if bot == "rock":
				hello.insert(END, " its draw\n")
			elif bot == "scissors":
					hello.insert(END, " player has won\n")
			elif bot == "paper":
						hello.insert(END, " Bot has won")
	hello.insert(END, x)
	x1 = "Bot is choosing...\n"
	hello.insert(END, x1)
	time()
def paper(hi):
	hello.insert(END, "Bot is choosing...\n")
	def idk():
			list6 = ["rock", "paper", "scissors"]
			bot = random.choice(list6)
			hello.insert(END, bot)
			if bot == "rock":
				hello.insert(END, " player has won\n")
			elif bot == "scissors":
					hello.insert(END, " bot has won\n")
			elif bot == "paper":
						hello.insert(END, " its draw\n")
	idk()
def scissors(cool):
	hello.insert(END, "Bot is choosing...\n")
	def wow():
			list6 = ["rock", "paper", "scissors"]
			bot = random.choice(list6)
			hello.insert(END, bot)
			if bot == "rock":
				hello.insert(END, " its draw\n")
			elif bot == "scissors":
					hello.insert(END, " player has won\n")
			elif bot == "paper":
						hello.insert(END, " Bot has won\n")
	wow()
	
def cleary():
	hello.delete('1.0', 'end')
nice = Label(mo, text = "ROCK, PAPER AND SCISSORS", font = ("calibre", 12))
nice.place(relx = 0.5, rely = 0.05, anchor = "center")
x = Button(mo, text = "Rock", padx = 50, pady = 25,background = '#d90833', command = lambda: rock("Rock\n"))
x.place(relx = 0.03, rely = 0.7)
y = Button(mo, text = "Paper", padx = 50, pady = 25,background = '#d90833', command = lambda: paper("paper\n"))
y.place(relx = 0.33, rely = 0.7)
#this is for the paper button ^
z = Button(mo, text = "scissors", padx = 50, pady = 25, background = '#d90833', command = lambda: scissors("scissors\n"))
z.place(relx = 0.65, rely = 0.7)
clear = Button(mo, text = "Clear", padx = 30, pady = 23, background = '#2cd9d9', command = cleary)
clear.place(relx = 0.1, rely = 0.6)
mo.mainloop()
