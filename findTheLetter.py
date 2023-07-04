while True:
    print("write done to end the program")
    word = input('Enter a word:')
    if word == "done":
        break
    while True:
        letter = input ('Enter a letter to search in the word:')
        if len(letter) > 1:
            print("please write just one letter")
            continue
        else:
            break
    num = 0
    for let in word:
        if let == letter:
            num +=1
        
    print(f'there is {num} "{letter}" in {word}')