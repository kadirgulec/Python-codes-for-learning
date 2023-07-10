from tabulate import tabulate
print("Beispiele für unstruktierte Daten")
header = ["Text" , "Grafik", "Bild", "Audio", "Video"]
data = [["Fließtext","Landkarte" , "Fotos","Musik","Film" ],
        ["Strukturierter Text", "3D-Modelle", "Röntgenbilder", "Sprache", "Videokonferenz"],
        ["Textsammlung", "Technische Zeichnung", "Satellitenbilder", "Geräusche", "Animation"],
        ["usw.","usw.","usw.","usw.","usw."]]

print(tabulate(data, headers = header, tablefmt = "fancy_grid", showindex = False))