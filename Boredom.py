import random
class main:
		def __init__(self, questions, info):
			self.questions = ["How are you?", "are you fine?"]
			self.info = []
		def function(self):
			qyy = input("Name: ")
			qts = int(input("age: "))
			qu = input("origin: ")
			self.info.append(qyy)
			self.info.append(qts)
			self.info.append(qu)
			d.search()
		def search(self):
			searchy = input("Search: ")
			if searchy == "calc":
				d.calc()
		def calc(self):
			def addition(x, y):
				return x + y
			def subtraction(x, y):
				return x - y
			def multiplication(x, y):
				return x * y
			def division(x, y):
				return x / y
			sel = int(input("select a math method: "))
			if sel == 1:
				calc_func = addition
			if sel == 2:
				calc_func = subtraction
			if sel == 3:
				calc_func = multiplication
			if sel == 4:
				calc_func = division
			int1 = int(input("Number1: "))
			int2 = int(input("Number2: "))
			print(calc_func(int1, int2))
class second:
				def __init__(self, character):
					self.character = ["deku", "naruto", "goku", "boruto"]
				def function(self):
					s = random.choice(self.character)
					doc = {"deku" : "boku no hero academia", "naruto" : "naruto shippuden", "goku" : "dragon ball", "boruto" : "Boruto"}
					print(s)
					sell = input("Guess the show: ")
					if s == "deku":
						if sell == doc["deku"]:
							print("correct")
						else:
							print("incorrect")
					if s == "naruto":
						if sell == doc["naruto"]:
							print("correct")
						else:
							print("incorrect")
					if s == "goku":
						if sell == doc["goku"]:
							print("correct")
						else:
							print("incorrect")
					if s == "boruto":
						if sell == doc["boruto"]:
							print("correct")
						else:
							print("incorrect")
d = second("unknown")
d.function()
				
				
			
			
			
		
