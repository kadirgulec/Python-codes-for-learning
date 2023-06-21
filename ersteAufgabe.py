#code von Kadir Gülec
print("Hallo ich lerne Python.")

print('Im ersten Schrit lernen wir \"Kopfsteuerte Schleife und else if\"')
name = input("Wie heißt du? ")
name = name.capitalize()
control = True
while control:
    uhr = input("Wie viel Uhr ist es? ")
    try:
        uhr = int(uhr)
        if uhr < 5:
            print (f'Gute Nacht {name}')
        elif uhr < 12:
            print (f'Guten Morgen {name}')
        elif uhr < 16:
            print(f'Guten Tag {name}')
        elif uhr < 21:
            print (f'Guten Abend {name}')
        elif uhr < 24:
            print(f'Gute Nacht {name}')
        else:
            print (f'Es ist aber lustig {name} :)')
        control = False
    except:
        print("Uhr muss ein Zahl sein")

print("jetzt lernen wir eine Mehrfachauswahl, fusgeschteuerte Schleife und Zählerschleife")
print (" jetzt werden wir die Zahl als text umsetzen")
print("und dann mit diesem zahl sterne geben") #auf Deutsch könnte ich leider das Satz nicht richtig aufbauen. Entschuldigung :(

number = input("Schreibe eine Zahl zwischen 1-5: ")

while True:
    try:
        number = int(number)
        match number:
            case 1:
                print("Eins")
            case 2:
                print("Zwie")
            case 3:
                print ("Drei")
            case 4:
                print("Vier")
            case 5:
                print ("Fünf")
            case _:
                print ("It is not zwischen 1-5")
                print ("aber trotzdem mache ich sterne :)")
        for x in range(number):
            print("*")
        break
    except:
        print("es muss ein Zahl sein")
        break




    
           
