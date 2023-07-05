""" i = 3
while i < 11:
    print (i * "*")
    i +=1
while i > 2:
    print (i * "*")
    i -= 1
 """

i = int(input("Wie Groß soll der Herz sein, mindestens 6 und gerade zahl"))

i2 = i + 1
firstZeile = i / 2
for zeile in range(i):  
    for spalte in range(i2):  
        if (zeile==0 and spalte == firstZeile - 2) or (zeile==0 and spalte == firstZeile + 2) or (zeile == 1 and spalte == firstZeile -3) or (zeile == 1 and spalte == firstZeile -1) or (zeile == 1 and spalte == firstZeile +1) or (zeile == 1 and spalte == firstZeile +3):  
            print("*",end=" ")  
        else:  
            print(end=" ")  
    print()

    #or(row==1 and col %3==0) or(row-col==2) or(row+col==8)