import time
import random
def dice_function(Name):
    while True:
        print("Type '!Roll' to roll the dice")
        type1 = input()
        if type1 != "!Roll":
            print("ERROR: You have written the name wrong")
        else:
            print("Dice is rolling...")
            time.sleep(4)
            select = [1, 2, 3, 4, 5, 6]
            player1 = random.choice(select)
            if player1 == 1:
                player1 = random.choice(select)
            if player1 == 2:
                player1 = random.choice(select)
            if player1 == 3:
                player1 = random.choice(select)
            if player1 == 4:
                player1 = random.choice(select)
            if player1 == 5:
                player1 = random.choice(select)
            if player1 == 6:
                player1 = random.choice(select)
            print(Name +"'s" + " dice number is ", player1)
        print("it's the bot's turn")
        time.sleep(2)
        bot = random.choice(select)
        if bot == 1:
            bot = random.choice(select)
        if bot == 2:
            bot = random.choice(select)
        if bot == 3:
            bot = random.choice(select)
        if bot == 4:
            bot = random.choice(select)
        if bot == 5:
            bot = random.choice(select)
        if bot == 6:
            bot = random.choice(select)
        print("bots dice number is ", bot)
        if bot == player1:
            print("it's draw")
        elif bot >= player1:
            print("bot has won this match")
        else:
            print("player has won this match")
        request = input("Play again (y/n)?")
        if request != "y":
            break
        else:
            return dice_function(Name)
while True:
    star = input("Type 'start' ")
    if star == "start":
        break
        continue 
namism = input("what's your name ")
if namism.isalpha() == True:
    dice_function(namism)
else:
    print("your name is invalid")
    
    

                        
    
    
    
