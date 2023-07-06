# define size n = even only
n = int(input("give the size of heart, min 8 and even numbers:"))
 
# so this heart can be made n//2 part left,
# n//2 part right, and one middle line
# i.e; columns m = n + 1
m = n+1
 
# loops for upper part
for i in range(n//2-1):
    for j in range(m):
         
        # condition for printing stars to upper line
        if i == n//2-2 and (j == 0 or j == m-1):
            print("*", end=" ")
             
        # condition for printing stars to left upper
        elif j <= m//2 and ((i+j == n//2-3 and j <= m//4) \
                            or (j-i == m//2-n//2+3 and j > m//4)):
            print("*", end=" ")
             
        # condition for printing stars to right upper
        elif j > m//2 and ((i+j == n//2-3+m//2 and j < 3*m//4) \
                           or (j-i == m//2-n//2+3+m//2 and j >= 3*m//4)):
            print("*", end=" ")
             
        # condition for printing spaces
        else:
            print(" ", end=" ")
    print()
 
# loops for lower part
for i in range(n//2-1, n):
    for j in range(m):
         
        # condition for printing stars
        if (i-j == n//2-1) or (i+j == n-1+m//2):
            print('*', end=" ")
                        
        # condition for printing spaces
        else:
            print(' ', end=" ")
             
    print()







""" i = 3
while i < 11:
    print (i * "*")
    i +=1
while i > 2:
    print (i * "*")
    i -= 1
 """

""" i = int(input("Wie Groß soll der Herz sein, mindestens 6 und gerade zahl"))

i2 = i + 1
firstZeile = i / 2
for zeile in range(i):  
    for spalte in range(i2):  
        if (zeile==0 and spalte == firstZeile - 2) or (zeile==0 and spalte == firstZeile + 2) or (zeile == 1 and spalte == firstZeile -3) or (zeile == 1 and spalte == firstZeile -1) or (zeile == 1 and spalte == firstZeile +1) or (zeile == 1 and spalte == firstZeile +3):  
            print("*",end=" ")  
        else:  
            print(end=" ")  
    print()
 """
    #or(row==1 and col %3==0) or(row-col==2) or(row+col==8)