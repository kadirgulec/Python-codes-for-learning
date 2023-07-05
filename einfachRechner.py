
while True:
    print('"q" to quit')
    #it will ask for the number 1 until the user gives an integer
    #if they type q, the program will exit
    while True:
        num1 = input("Geben Sie die erste Zahl ein:")
        if num1 == "q":
            exit()
        try:
            num1 = int(num1)
            break
        except:
            print("Sie müssen eine Zahl geben")
            continue
    while True:
        num2 = input("Geben Sie die zweite Zahl ein:")
        if num2== "q" :
            exit()
        try:
            num2 = int(num2)
            break
        except:
            print("Sie müssen eine Zahl geben")
            continue
    #it will control the operator and make the calculation depended from the operator, that the user typed, if the 
    # user types something else than 4 operators it will ask again
    while True:
        operator = input("Geben Sie einen Operator an + - * /:")
        if operator =="q":
            exit()
        if operator != "+" and  operator != "-" and operator != "*" and operator != "/" :
            print("Operator muss +,-,* oder / sein")
            continue
        elif operator == "+":
            ergebniss = num1 + num2
            break
        elif operator == "-":
            ergebniss = num1 - num2
            break
        elif operator == "*":
            ergebniss = num1 * num2
            break
        elif operator == "/":
            #it will give a traceback if the user try to division something with 0
            # so it will be controlled here
            try:
                ergebniss = num1 / num2
                break
            except:
                print("Zahlen können nicht durch 0 geteilen")
                ergebniss = "nicht möglich"
                break
        else:
            break

    print(f'Das Ergebnis von {num1} {operator} {num2} ist : {ergebniss}')
