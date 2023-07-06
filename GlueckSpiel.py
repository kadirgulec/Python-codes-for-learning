import random
symbolen = ("♣" , "♡" ,"♢", "♠", "♤", "♥","♦","♧", "a", "b")
#turnTheWheel = True
totalPoint = 0
while True:
    turnTheWheel = input("Dreh das Rad? \n'y' oder 'n' eingeben: ")
    if turnTheWheel == "n":
        if totalPoint < 0:
            print(f'Pecht gehabt :( {totalPoint} Punkte')
        else:
            print(f'Sie haben {totalPoint} Punkte gewonnen')
        break
    elif turnTheWheel == "y":
        symbol_1 = random.choice(symbolen)
        symbol_2 = random.choice(symbolen)
        symbol_3 = random.choice(symbolen)
        print(symbol_1,symbol_2,symbol_3)
        if (symbol_1 == symbol_2) and (symbol_2 == symbol_3):
            totalPoint += 1000
        elif (symbol_1 == symbol_2) or (symbol_1 == symbol_3) or (symbol_2 == symbol_3 ):
            totalPoint += 50
        else:
            totalPoint -= 10
        print (f'Total Punkt : {totalPoint}')
    else:
        print("Sie müssen y oder n schreiben")
        continue
    

