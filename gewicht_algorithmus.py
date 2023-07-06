

def findBMI():
    while True: #asking the user his weight and controlling if it is a number
        gewicht = input("Gewicht: ")
        if gewicht == "q":
            bmi = False
            exit()
        try:
            gewicht = int(gewicht)
            break
        except:
            print("Es muss ein Zahl gegeben werden")
            continue
    while True: #asking user his height and controlling if it is a number
        koerpergroesse = input ("Körpergröße: ")
        if koerpergroesse == "q":
            bmi = False
            exit()
        try:
            koerpergroesse = float(koerpergroesse)
            break
        except:
            print("Es muss ein Zahl gegeben werden")
            continue 

    while gewicht < 50 or gewicht > 150 or koerpergroesse > 2 or koerpergroesse < 1.5 : #a loop to ask the weight and height until the user gives the numbers in range i want to
        
        if gewicht < 50 or gewicht > 150:
            print("Gewicht muss zwischen 50-150 sein")
            gewicht = input("Gewicht: ")
            gewicht = int(gewicht)
        else:
            print("Körpergröße muss zwischen 1.5-2 sein")
            koerpergroesse = input("Körpergröße: ")
            koerpergroesse = float(koerpergroesse)
    bmi = gewicht/(koerpergroesse * koerpergroesse)
    idealMin = koerpergroesse * koerpergroesse * 18.6
    idealMax = koerpergroesse * koerpergroesse * 24.9

    bmiDictionary ={
        'bmi' : bmi,
        'idealMin' : idealMin,
        'idealMax' : idealMax
    }
    return bmiDictionary

def bmiToString(bmi): #it changes the bmi to the meaning of it
    try:
        bmi = float(bmi)
    except:
        print("Es gibt ein Fehler")
    if bmi == False:
        exit()
    elif bmi <= 16:
        return "starkes Untergewicht"
    elif bmi < 17:
        return "maßiges Untergewicht"
    elif bmi < 18.5:
        return "leichter Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 30:
        return "Präadipositas (Übergewicht)"
    elif bmi < 35:
        return "Adipositas Grad I"
    elif bmi < 40:
        return "Adipositas Grad II"
    else:
        return "Adipositas Grad III"
    
control = True 
while control != False:
    bmi = findBMI()
    bmiZ = bmi['bmi']
    stringBmi = bmiToString(bmiZ)
    #das idealGewicht Idea habe ich von Yavuz genommen :D
    idealMin = bmi['idealMin']
    idealMax = bmi['idealMax']
    print(f'Sie sind {stringBmi}, und Ihre BMI ist : {bmiZ} \nIhre Idealgewicht ist zwischen {idealMin}-{idealMax}')
    control = bmiZ
