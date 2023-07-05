# einfachste version
""" print('Vorname\t\tNachname\t\tBildungsträger')
print('Kadir\t\tGülec\t\tEVB')
print('Yavuz\t\tGürdal\t\tEVB')
print('Patrick\t\tWolfsberger\tEVB')
print('Sonja\t\tLasar\t\tEVB')
print('Zekiye\t\tÖztürk\t\tEVB') """


from tabulate import tabulate

data = [["Kadir", "Gülec"], 
        ["Patrick", "Wolfsberger"], 
        ["Yavuz", "Gürdal"], 
        ["Zekiye", "Öztürk"],
        ["Sonja", "Lasar"]]
  
#define header names
col_names = ["Vorname", "Name"]
  
#display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex="always"))


