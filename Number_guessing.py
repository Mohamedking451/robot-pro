import random
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = (random.choice(list5) + random.choice(list5))
S = (random.choice(list5) * random.choice(list5))
G = (random.choice(list5) / random.choice(list5))
Fall = [N, S, G]
while True:
	for x in Fall:
		if x > 50:
		  	 print(x)
		  	 print("its larger than then 50")
		elif x < 50:
		   print("its smaller than 50")
		try:
			question_n = int(input("guess the number"))
		except:
			print("you have written a non-digit please try again")
			break
		for y in Fall:
					if x != question_n:
						print("incorrect")
						print(question_n, "does not equal ", x)
						break
						continue
					else:
						print("correct")
						print(question_n, "does equal to", x)
		quest1 = input("wanna play again? (y/n)")
		if quest1.lower() != "yes":
			print(None)
		else:
			break
	
