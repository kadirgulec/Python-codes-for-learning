name = input("Wie heißen Sie:")
# asking the income
while True:
    einkommen = input("Wie hoch ist Ihr Einkommen:")
    try:
        einkommen = float(einkommen)
        break
    except:
        print("Einkommen muss Zahl sein")
        continue
# find the tax rate function
def steuersatz(einkommen):
    if einkommen <= 10000:
        return 0.4
    elif einkommen <= 30000:
        return 0.55
    elif einkommen <= 70000:
        return 0.75
    else:
        return 0.82


strstz = steuersatz(einkommen) #make a variable with tax rate function
steure = einkommen * strstz # how much must be the tax

def germanCurrencyStlye(number):
    number = round(number,2)
    number = str(number).split(".")
    i = 1
    n = 1 #to increase the index number with dots
    formatedNumber = "nothing"
    while i < len(number[0]):
        if i % 3  == 0:
            
            if formatedNumber != "nothing": #if i have a formatedNumber i have to change it from that not anymore with number variable
                a = i + n #to find the true index position I added i and n (i adde 1 to n everytime i added a dot)
                formatedNumber = formatedNumber[:-a] + "." + formatedNumber[-a:]
                n += 1 #every time when a dot is added, the number will have one more dot, deshalb i have to add 1 more 
            else: #if there is not formatedNumber yet, i format it with number variable
                formatedNumber = number[0][:-i] + "." + number[0][-i:]
                
        i += 1
    if len(number[1]) < 2: #after komma, i want two numbers, so if it is one i will add one zero at end
        number[1] = number[1] + "0"
    """ print (formatedNumber) """
    numberDublo = formatedNumber + "," + number[1]
    return numberDublo

einkommen = germanCurrencyStlye(einkommen)
steure = germanCurrencyStlye(steure)

print(f'Ihr Einkommen ist {einkommen}€ und steuersatz ist {strstz*100}%. Sie müssen {steure}€ steuer Zahlen')