

def findBMI():
    gewicht = input("Gewicht: ")
    koerpergroesse = input ("Körpergröße: ")
    try:
        gewicht = int(gewicht)
    except:
        print("Es muss ein Zahl gegeben werden")
        exit()
    try:
        koerpergroesse = float(koerpergroesse)
    except:
        print("Es muss ein Zahl gegeben werden")
        exit() 

    while gewicht < 50 or gewicht > 150 or koerpergroesse > 2 or koerpergroesse < 1.5 :
        
        if gewicht < 50 or gewicht > 150:
            print("Es muss zwischen 50-150 sein")
            gewicht = input("Gewicht: ")
            gewicht = int(gewicht)
        else:
            print("Es muss zwischen 1.5-2 sein")
            koerpergroesse = input("Körpergröße: ")
            koerpergroesse = float(koerpergroesse)
    bmi = gewicht/koerpergroesse
    print(bmi)

findBMI()
