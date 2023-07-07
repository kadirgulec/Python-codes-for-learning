def monatsumsatzFragen():
    i = 0
    global monatsumsatz
    global jahresUmsatz
    monatsumsatz = []
    while i <= 11:
        monat = input(f'Umsatz für Monat {i+1}:')
        try:
            monat = float(monat)
        except:
            print("Bitte Zahl geben")
            continue
        monatsumsatz.append(monat)
        i += 1
    counter = 1 #this counts the monats for asking 
    for a in monatsumsatz:
        print (f'Monat {counter} = {a}')
        counter += 1
    while True:
        istMonatsRichtig = input("Sind alle Monatsumsatz richtig eingeschrieben (j/n)\n: ")
        if istMonatsRichtig == "n":
            monatsumsatzFragen() #when the user typed something wrong, he can start the function again by typing n
            break
        elif istMonatsRichtig == "j":
            break
        elif istMonatsRichtig == "e":
            exit()
        else:
            print("Bitte j/n oder e für ende")
            continue

    jahresUmsatz = jahresumsatz(monatsumsatz)


def jahresumsatz (monatsumsatz):
    total = 0
    for monat in monatsumsatz:
        total += int(monat)
    return total

def checkBonus(monatsumsatz):
    if checkMonatsMehr(monatsumsatz):
        return 0.018
    elif checkQuartalsumsatz(monatsumsatz) == False: #if NOT einer der vier Quartalsumsätze mehr als 10% unter dem Jahresdurchschnitt der Quartalsumsätze liegt
        if jahresUmsatz < 18000:
            return 0.03
        elif jahresUmsatz < 20000:
            return 0.05
        else:
            return 0.065
    else:
        if jahresUmsatz < 18000:
            return 0.05
        elif jahresUmsatz < 20000:
            return 0.09
        else:
            return 0.12


def checkQuartalsumsatz(monatsumsatz):
    quartalumsatz = []
    quartal1= 0
    quartal2= 0
    quartal3= 0
    quartal4= 0
    counter = 1
    for i in monatsumsatz: #makes an array with quartalumsätze
        if counter <= 3:
            quartal1 += i
            counter += 1
        elif counter <= 6:
            quartal2 += i
            counter +=1
        elif counter <= 9:
            quartal3 += i
            counter += 1
        else:
            quartal4 += i
    quartalumsatz.append(quartal1)
    quartalumsatz.append(quartal2)
    quartalumsatz.append(quartal3)
    quartalumsatz.append(quartal4)
    jahresdurschnittQ = jahresUmsatz / 4
    for quartal in quartalumsatz: #looks all quartals and compare them with the Jahresdurschnitt of the Quartals 
        if quartal/jahresdurschnittQ < 0.1:
            return True
        else:
            continue
    return False
            
def checkMonatsMehr(monatsumsatz): # check if einer der 12 Monatsumsätze mehr als 70 % unter dem Jahresdurchschnitt der Monatsumsätze liegt
    monatlicheDurchnitt = jahresUmsatz/12
    for monat in monatsumsatz:
        if monat/monatlicheDurchnitt < 0.7:
            return True
        else:
            continue
    return False

monatsumsatzFragen()
bonusRate = checkBonus(monatsumsatz)
bonusGeld = jahresUmsatz * bonusRate

print(f'Jahresumsatz: {jahresUmsatz}€')
if checkMonatsMehr(monatsumsatz):
    print(f'Weil einer der 12 Monatsumsätze mehr als 70 % unter dem Jahresdurchschnitt der Monatsumsätze liegt, erhalten Sie nur 1,8% Bonus')
elif checkQuartalsumsatz(monatsumsatz):
    print(f'Weil einer der vier Quartalsumsätze mehr als 10% unter dem Jahresdurchschnitt der Quartalsumsätze liegt erhalten Sie mehr als normal Bonus')
print("-------------------------------------")
print(f'Bonus Prozent: {bonusRate * 100}%')
print(f'Bonus in Geld: {bonusGeld}€')

#Bitte nach hier nicht lesen, ich versuche was anders hier :)

""" while True:
    istMonatsumsatzBekannt = input("Wissen Sie ob einer der 12 Monatsumsätze mehr als 70% unter dem Jahresdurchnitt der Monatsumsätzte liegt (j/n)\n: ") 
    istMonatsumsatzBekanntSub = ""
    if istMonatsumsatzBekannt == "n":
        print("Sie müssen jeden Monatsumsätze eingeben.")
        while True: #I wanted to ask again if the user is sure to give all 12 Months revenue, it might be tiring :)
            istMonatsumsatzBekanntSub = input("w = weiter \ne = ende\nr = restart\n: ")
            if istMonatsumsatzBekanntSub == "w":
                monatsumsatzFragen()
                break
            elif istMonatsumsatzBekanntSub == "e":
                exit()
            elif istMonatsumsatzBekanntSub == "r":
                break
            else:
                print ("w, q oder r schreiben")
                continue
        if istMonatsumsatzBekanntSub == "r":
            continue
    elif istMonatsumsatzBekannt == "j":
        istJahresumsatzBekannt = input("Wissen Sie die Jahresumsatz (j/n)\n: ")
        if istMonatsumsatzBekanntSub == "w":
            break
        elif istJahresumsatzBekannt == "n":
            print("Sie müssen jeden Monatsumsätze eingeben.")
            while True:
                istJahresumsatzBekanntSub = input("w = weiter \ne = ende\nr = restart\n: ")
                if istJahresumsatzBekanntSub == "w":
                    monatsumsatzFragen()
                    break
                elif istJahresumsatzBekanntSub == "e":
                    exit()
                elif istJahresumsatzBekanntSub == "r":
                    break
                else:
                    print ("w, q oder r schreiben")
                    continue
            if istJahresumsatzBekanntSub == "r":
                continue
        elif istJahresumsatzBekannt == "j":
            while True:
                monatsUmsatzUnter = input("liegt einer der 12 Monatsumsätze mehr als 70% unter dem Jahresdurchnitt der Monatsumsätzte (j\n)\n: ")
                if monatsUmsatzUnter == "j" or monatsUmsatzUnter == "n":
                    break
                elif monatsUmsatzUnter == "e":
                    exit()
                else:
                    print("Bitte j/n oder e für ende")
                    continue
                
            while True:
                jahresUmsatz = input("Wie viel ist der Jahresumsatz: ")
                try:
                    jahresUmsatz = float(jahresUmsatz)
                    break
                except ValueError:
                    print("Bitte nur Zahlen eingeben und Cents mit Punkt trennen")
                    continue
        elif istJahresumsatzBekannt == "e":
            exit()
        else:
            print("j/n oder e für ende")
            continue
    elif istMonatsumsatzBekannt == "e":
        exit()
    else:
       print("j/n oder e für ende")
       continue
    break """
            

