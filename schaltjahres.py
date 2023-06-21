print ("Wie viel Tage gibt es in Februar in besonderes Jahr")

while True:
    jahr = input("Geben Sie ein Jahr: ")

    try:
        jahr = int(jahr)
        if jahr % 4 == 0:
            februar = 29
            if jahr % 100 == 0:
                februar = 28
                if jahr % 400 == 0:
                    februar = 29
        else:
            februar= 28
        print (f'Es gibt {februar} Tagen im Februar {jahr}')
        break
    except:
        print("Sie müssen ein Zahl geben")