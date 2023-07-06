set1 = set()
set2 = set()
set1i = 1
set2i = 1
while True:
    item = input(f'({set1i}) Geben Sie 1 Zahl für die Menge (1) ("q" ende): ')
    if item == "q":
        break
    set1.add(item)
    set1i += 1
    print(set1)

while True:
    item = input(f'({set2i}) Geben Sie 1 Zahl für die Menge (2) ("q" ende): ')
    if item == "q":
        break
    set2.add(item)
    set2i += 1
    print(set2)

print(f'Schnitmenge: {set1 & set2}')
print(f'Vereinigungsmenge: {set1 | set2}')
print(f'Differenzmenge Menge1: {set1 - set2}')
print(f'Differenzmenge Menge2: {set2 - set1}')
print(f'Symmmetrische Differenz: {set1 ^ set2}')
print(f'Ist Menge 1 Obermenge von Menge 2: {set1 > set2}')
print(f'Ist Menge 2 Obermenge von Menge 1: {set2 > set1}')