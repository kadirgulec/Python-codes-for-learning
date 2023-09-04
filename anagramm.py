
def anagram(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()
    text1 = sorted(text1)
    text2 = sorted(text2)
    if text1 == text2:
        return True
    else:
        return False
    
while True:
    print ('q für exit')
    text1 = input('Erste:')
    if text1 == 'q':
        break
    text2 = input('Zwite:')
    if text2 == 'q':
        break
    elif anagram(text1,text2):
        print(f'{text1} und {text2} sind Anagramms')
    else:
        print(f'{text1} und {text2} sind kein Anagramms')