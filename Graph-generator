from tkinter import *
import matplotlib.pyplot as plt
mo = Tk()
X1 = IntVar()
Y1 = IntVar()
def start_button():
	start()
def graph_button():
	try:
		coordination_X = [X1.get()]
		coordination_Y = [Y1.get()]
		plt.plot(coordination_X, coordination_Y,linewidth = 5)
		plt.show()
	except:
		screen10 = Toplevel(mo)
		screen10.geometry("650x650")
		Xi = Label(screen10, text = "THERES SOMETHING WRONG WITH UR COORDINATION, TRY AGAIN", fg = "red")
		Xi.place(relx = 0.5, rely= 0.5, anchor = "center")
def start():
	button5.forget()
	X = Label(mo, text = "Plot the X and Y coordination")
	X.pack()
	try:
		Plot_X = Entry(mo, width = 30, textvariable = X1).place(relx = 0.5, rely = 0.5, anchor = "center")
		Plot_Y = (Button(mo, ))
		button1 = Button(mo, height = 1, width = 10, text = "launch graph", command = graph_button)
		button1.pack()
	except:
		error = Label(mo, text = "YOU HAVENT PROPERLY PLOTTED THE GRAPH")
		error.place(relx = 0.5, rely = 0.5)
button5 = Button(mo, height = 1, width = 10, text = "START", command = start)
button5.place(relx = 0.5 , rely = 0.5 , anchor = "center")
button5.pack()
mo.mainloop()

