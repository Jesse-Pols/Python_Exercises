def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')

lijst = ['d', 'e', 'f']

print(lijst)
wijzig(lijst)
print(lijst)

## ['d', 'e', 'f'] is een object en kan als geheel object aan de list toegevoegd worden. Een list in de list als het ware, wat niet de bedoeling is. Daarom moeten 'd', 'e' en 'f' apart toegevoegd worden.
## De wijzig() functie werkt niet met een string parameter, omdat de clear() en append() functies specifiek voor lists zijn.
## Een string is een immutable object, en kan niet vanuit een functie gewijzigd worden.

