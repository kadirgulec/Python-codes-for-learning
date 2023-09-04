""" word = input("Geben Sie ein Wort, um zu überprüfen, ob es Palindrom ist:")
word = word.lower()
word = word.replace(' ','')
if word == word[::-1]:
    print("es ist ein Palindrom")
else:
    print("es ist kein Palindrom") """

def palindrom():
    print ('Tippen Sie s zum stoppen')
    global word
    word = input("Geben Sie ein Wort, um zu überprüfen, ob es Palindrom ist:")
    word = word.lower()
    word =''.join(word.split())
    if word == 's':
        exit()
    elif word == word[::-1]:
        print("es ist ein Palindrom")
    else:
        print("es ist kein Palindrom")

while True:
    palindrom()