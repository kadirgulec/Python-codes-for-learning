word = input('Enter a word:')
letter = input ('Enter a letter to search in the word:')
num = 0
for let in word:
    if let == letter:
        num +=1
    
print(f'there is {num} "{letter}" in {word}')